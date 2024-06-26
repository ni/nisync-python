<%
    from _metadata.constants import error_codes
%>\
# This file was generated

from nisync.enums import CtypesEnum


class Status(CtypesEnum):
%   for error in error_codes:

    #: ${error['message']}
    #:
    #: #define NISYNC_ERROR_${error['alt_symbol']} = ${error['comment']}
    #:
    #: nisyncerr_${error['symbol']} = ${error['code']}
    ${error['py_symbol']} = ${error['code']}
%   endfor
