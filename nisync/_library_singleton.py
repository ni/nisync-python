import ctypes
import platform
import threading

from nisync import _library, errors

_instance = None
_instance_lock = threading.Lock()
_library_info = {
    "Linux": {
        "32bit": {"name": "libnisync.so", "type": "cdll"},
        "64bit": {"name": "libnisync.so", "type": "cdll"},
    },
    "Windows": {
        "32bit": {"name": "nisync.dll", "type": "windll"},
        "64bit": {"name": "nisync.dll", "type": "cdll"},
    },
}


def _get_library_name():
    try:
        return _library_info[platform.system()][platform.architecture()[0]]["name"]
    except KeyError:
        raise errors.UnsupportedConfigurationError


def _get_library_type():
    try:
        return _library_info[platform.system()][platform.architecture()[0]]["type"]
    except KeyError:
        raise errors.UnsupportedConfigurationError


def get():
    """Returns a singleton instance of the nisync library."""
    global _instance
    global _instance_lock

    with _instance_lock:
        if _instance is None:
            try:
                library_type = _get_library_type()
                if library_type == "windll":
                    ctypes_library = ctypes.WinDLL(_get_library_name())
                else:
                    assert library_type == "cdll"
                    ctypes_library = ctypes.CDLL(_get_library_name())
            except OSError:
                raise errors.DriverNotInstalledError()
            _instance = _library.Library(ctypes_library)
    return _instance
