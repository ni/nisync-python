<%
    from _metadata import functions
%>\
# This file was generated

import ctypes
import threading
from nisync._visatype import *  # noqa: F403


def ascii_encode(value):
    if isinstance(value, str):
        return value.encode('ascii')
    return value


class Library(object):
    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
%   for name in functions:
        self.niSync_${name}_cfunc = None
%   endfor
%   for name, func in functions.items():
<%
        c_func_name = 'niSync_' + name
        argtypes = ', '.join(
            {
                'in': param['type'],
                'out': 'ctypes.POINTER({})'.format(param['type']),
            }[param['direction']]
            for param in func['parameters']
        )
        parameters = ', '.join(param['name'] for param in func['parameters'])

        parameters_cfunc_list = []
        for param in func['parameters']:
            if param['type'] in ['ViString', 'ViRsrc', 'ViConstString'] and param['direction'] == 'in':
                parameters_cfunc_list.append("ascii_encode({})".format(param['name']))
            else:
                parameters_cfunc_list.append(param['name'])
        parameters_cfunc = ', '.join(parameters_cfunc_list)
%>\

## FIXME(python_api): Fix N803 - argument name '<name>' should be lowercase
    def ${c_func_name}(self, ${parameters}):  # noqa: N802,N803
        with self._func_lock:
            if self.${c_func_name}_cfunc is None:
                self.${c_func_name}_cfunc = self._library.${c_func_name}
                self.${c_func_name}_cfunc.argtypes = [${argtypes}]  # noqa: F405
                self.${c_func_name}_cfunc.restype = ${func['returns']}  # noqa: F405
        return self.${c_func_name}_cfunc(${parameters_cfunc})
%   endfor