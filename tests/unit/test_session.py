import pytest

import nisync
import nisync._library_singleton
from nisync._visatype import ViBoolean, ViSession
from nisync.constants import OSCILLATOR, PXI_CLK10_IN

try:
    from unittest import mock
except ImportError:
    import mock


class CtypesMatcher(object):
    """A matcher class for comparing ctypes objects or values."""

    def __init__(self, value, ctype):
        """Initializes the CtypesMatcher."""
        self.value = value
        self.ctype = ctype

    def __eq__(self, other):
        """Compares the CtypesMatcher's value with another object or value."""
        if hasattr(other, "value"):
            return other.value == self.value
        return other == self.value

    def __repr__(self):
        """Represents the CtypesMatcher's value as a string using its ctype."""
        return "{}".format(self.ctype(self.value))


RESOURCE_NAME = "MockResource"
SESSION_HANDLE = CtypesMatcher(1, ViSession)

VI_FALSE = CtypesMatcher(0, ViBoolean)
VI_TRUE = CtypesMatcher(1, ViBoolean)


def init_mock(resource_name, id_query, reset_device, vi):
    vi.contents.value = SESSION_HANDLE.value
    return 0


def error_message_mock(vi, status, message):
    message.value = b"dumping error message"
    return 0


@pytest.fixture
def lib_mock(mocker):
    platform_system_mock = mocker.patch("platform.system")
    platform_system_mock.return_value = "Linux"

    platform_architecture_mock = mocker.patch("platform.architecture")
    platform_architecture_mock.return_value = ("64bit", "ELF")

    ctypes_mock = mocker.patch("ctypes.CDLL")
    lib = ctypes_mock.return_value
    lib.__enter__.return_value = lib
    lib.niSync_init.side_effect = init_mock
    lib.niSync_close.return_value = 0
    lib.niSync_error_message.side_effect = error_message_mock
    # Reset the singleton instance to avoid side effects between tests
    nisync._library_singleton._instance = None
    yield lib
    nisync._library_singleton._instance = None


def test___session___open_and_close___succeeds(lib_mock):
    session = nisync.Session(RESOURCE_NAME)
    session.close()

    expected_calls = [
        mock.call.niSync_init(RESOURCE_NAME.encode(), VI_FALSE, VI_FALSE, mock.ANY),
        mock.call.niSync_close(SESSION_HANDLE),
    ]
    assert lib_mock.mock_calls == expected_calls


def test___session___open_with_context_manager___succeeds(lib_mock):
    with nisync.Session(RESOURCE_NAME):
        ...

    expected_calls = [
        mock.call.niSync_init(RESOURCE_NAME.encode(), VI_FALSE, VI_FALSE, mock.ANY),
        mock.call.niSync_close(SESSION_HANDLE),
    ]
    assert lib_mock.mock_calls == expected_calls


def test___session___open_when_init_fails___raises_driver_error(lib_mock):
    def init_error_mock(resource_name, id_query, reset_device, vi):
        vi.contents.value = SESSION_HANDLE.value
        return nisync.errors.Status.DEVICE_NOT_FOUND

    lib_mock.niSync_init.side_effect = init_error_mock

    with pytest.raises(nisync.errors.DriverError) as exc:
        session = nisync.Session(RESOURCE_NAME)
        session.close()

    assert exc.value.code == nisync.errors.Status.DEVICE_NOT_FOUND


def test___session___open_with_context_manager_when_init_fails___raises_driver_error(lib_mock):
    def init_error_mock(resource_name, id_query, reset_device, vi):
        vi.contents.value = SESSION_HANDLE.value
        return nisync.errors.Status.DEVICE_NOT_FOUND

    lib_mock.niSync_init.side_effect = init_error_mock

    with pytest.raises(nisync.errors.DriverError) as exc:
        with nisync.Session(RESOURCE_NAME):
            ...

    assert exc.value.code == nisync.errors.Status.DEVICE_NOT_FOUND


def test___session___open_with_reset___succeeds(lib_mock):
    with nisync.Session(RESOURCE_NAME, reset_device=True):
        ...

    expected_calls = [
        mock.call.niSync_init(RESOURCE_NAME.encode(), VI_FALSE, VI_TRUE, mock.ANY),
        mock.call.niSync_close(SESSION_HANDLE),
    ]
    assert lib_mock.mock_calls == expected_calls


def test___session___reset___succeeds(lib_mock):
    lib_mock.niSync_reset.return_value = 0

    with nisync.Session(RESOURCE_NAME) as session:
        session.reset()

    expected_calls = [
        mock.call.niSync_init(RESOURCE_NAME.encode(), VI_FALSE, VI_FALSE, mock.ANY),
        mock.call.niSync_reset(SESSION_HANDLE),
        mock.call.niSync_close(SESSION_HANDLE),
    ]
    assert lib_mock.mock_calls == expected_calls


def test___session___self_test___succeeds(lib_mock):
    def self_test_mock(vi, test_result, test_message):
        test_result.value = 0
        test_message.value = b""
        return 0

    lib_mock.niSync_self_test.side_effect = self_test_mock

    with nisync.Session(RESOURCE_NAME) as session:
        result, message = session.self_test()

    assert result == 0
    assert message == ""
    expected_calls = [
        mock.call.niSync_init(RESOURCE_NAME.encode(), VI_FALSE, VI_FALSE, mock.ANY),
        mock.call.niSync_self_test(SESSION_HANDLE, mock.ANY, mock.ANY),
        mock.call.niSync_close(SESSION_HANDLE),
    ]
    assert lib_mock.mock_calls == expected_calls


def test___session___connect_clock_terminals___succeeds(lib_mock):
    lib_mock.niSync_ConnectClkTerminals.return_value = 0

    with nisync.Session(RESOURCE_NAME) as session:
        session.connect_clock_terminals(source=OSCILLATOR, destination=PXI_CLK10_IN)

    expected_calls = [
        mock.call.niSync_init(RESOURCE_NAME.encode(), VI_FALSE, VI_FALSE, mock.ANY),
        mock.call.niSync_ConnectClkTerminals(
            SESSION_HANDLE, OSCILLATOR.encode(), PXI_CLK10_IN.encode()
        ),
        mock.call.niSync_close(SESSION_HANDLE),
    ]
    assert lib_mock.mock_calls == expected_calls


def test___session___disconnect_clock_terminals___succeeds(lib_mock):
    lib_mock.niSync_DisconnectClkTerminals.return_value = 0

    with nisync.Session(RESOURCE_NAME) as session:
        session.disconnect_clock_terminals(source=OSCILLATOR, destination=PXI_CLK10_IN)

    expected_calls = [
        mock.call.niSync_init(RESOURCE_NAME.encode(), VI_FALSE, VI_FALSE, mock.ANY),
        mock.call.niSync_DisconnectClkTerminals(
            SESSION_HANDLE, OSCILLATOR.encode(), PXI_CLK10_IN.encode()
        ),
        mock.call.niSync_close(SESSION_HANDLE),
    ]
    assert lib_mock.mock_calls == expected_calls


def test___session___compare_session_handle___succeeds(lib_mock):
    session = nisync.Session(RESOURCE_NAME)
    assert session.session_handle == SESSION_HANDLE.value
    session.close()

    expected_calls = [
        mock.call.niSync_init(RESOURCE_NAME.encode(), VI_FALSE, VI_FALSE, mock.ANY),
        mock.call.niSync_close(SESSION_HANDLE),
    ]
    assert lib_mock.mock_calls == expected_calls
