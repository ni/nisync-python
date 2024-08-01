import pytest

from nisync import Session
from nisync._errorcodes import Status
from nisync.errors import DriverError


@pytest.mark.parametrize("reset_device", [True, False])
def test___open_session_with_reset___close_session(resource_name, reset_device):
    session = Session(resource_name, reset_device)
    session.close()


@pytest.mark.parametrize(
    "resource_name, error_type, error_code", [("FakeDevice", DriverError, Status.DEVICE_NOT_FOUND)]
)
def test___open_session___invalid_resource_name___assert_expected_error(resource_name, error_type, error_code):
    with pytest.raises(error_type) as expected_info:
        session = Session(resource_name, True)
        session.close()
    assert expected_info.value.code == error_code
