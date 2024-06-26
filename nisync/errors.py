import platform
import warnings

from nisync._errorcodes import Status


def _is_success(code):
    return code == 0


def _is_error(code):
    return code < 0


def _is_warning(code):
    return code > 0


class Error(Exception):
    def __init__(self, message):
        super(Error, self).__init__(message)


class DriverError(Error):
    def __init__(self, code, description):
        assert _is_error(code), "Should not raise Error if code is not fatal."
        self.code = code
        self.description = description
        super(DriverError, self).__init__(str(self.code) + ": " + self.description)


class DriverWarning(Warning):
    def __init__(self, code, description):
        assert _is_warning(code), "Should not create Warning if code is not positive."
        super(DriverWarning, self).__init__(
            "Warning {0} occurred.\n\n{1}".format(code, description)
        )


class UnsupportedConfigurationError(Error):
    def __init__(self):
        super(UnsupportedConfigurationError, self).__init__(
            "System configuration is unsupported: "
            + platform.architecture()[0]
            + " "
            + platform.system()
        )


class DriverNotInstalledError(Error):
    def __init__(self):
        super(DriverNotInstalledError, self).__init__(
            "The NI-DMM runtime could not be loaded. Make sure it is installed and its bitness matches that of your Python interpreter. Please visit http://www.ni.com/downloads/drivers/ to download and install it."
        )


def _lookup_error_code(code):
    try:
        return Status(code)
    except ValueError:
        # code is not in the nisync error codes enum
        return code


def handle_error(session, code, ignore_warnings=False, is_error_handling=False):
    if _is_success(code) or (_is_warning(code) and ignore_warnings):
        return

    code_to_use = _lookup_error_code(code)
    if is_error_handling:
        # The caller is in the midst of error handling and an error occurred.
        # Don't try to get the description or we'll start recursing until the stack overflows.
        description = ""
    else:
        if isinstance(code_to_use, Status):
            description = session._get_error_description(code_to_use)
        else:
            description = ""

    if _is_error(code_to_use):
        raise DriverError(code_to_use, description)

    assert _is_warning(code_to_use)
    warnings.warn(DriverWarning(code_to_use, description))


warnings.filterwarnings("always", category=DriverWarning)
