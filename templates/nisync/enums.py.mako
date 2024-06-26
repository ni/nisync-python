<%
    from _metadata import constants
    import re

    enum_patterns = {
        'UpdateEdge':                  (r'UPDATE_EDGE_(.+)', r'\1'),
        'InitialTimeSource':           (r'INIT_TIME_SRC_(.+)', r'\1'),
        'Level':                       (r'LEVEL_(.+)', r'\1'),
        'Edge':                        (r'EDGE_(.+)', r'\1'),
        'IEEE1588PortState':           (r'IEEE_1588_CLK_STATE_(.+)', r'\1'),
        'SyncInterval':                (r'SYNC_INTERVAL_(.+)', r'\1'),
        'IEEE1588ClockAccuracy':       (r'IEEE_1588_CLK_ACCURACY_(.+)', r'\1'),
        'IEEE1588ClockClass':          (r'IEEE_1588_CLK_CLASS_(.+)', r'\1'),
        'IEEE8021ASClockAccuracy':     (r'IEEE_8021AS_CLK_ACCURACY_(.+)', r'\1'),
        'IRIGType':                    (r'IRIG_TYPE_(.+)', r'\1'),
        'GPSStatus':                   (r'GPS_(.+)', r'\1'),
        'TimeReference':               (r'TIMEREF_(.+)', r'\1'),
        'BMCAMode':                    (r'BMCA_MODE_(.+)', r'\1'),
        'IEEE8021ASPortState':         (r'IEEE_8021AS_PORT_STATE_(.+)', r'\1'),
        'ExternalCalibrationAction':   (r'EXT_CAL_(.+)', r'\1'),
        'LogicBlockOperation':         (r'LOGIC_BLOCK_(.+)_OPERATION', r'\1'),
    }
%>\
# This file was generated

from enum import IntEnum


class CtypesEnum(IntEnum):
    @classmethod
    def from_param(cls, obj):
        return int(obj)
%   for class_name, pattern in sorted(enum_patterns.items()):
<%
        enum_data = {k: v for k, v in constants.items() if re.match(pattern[0], k)}
        if not enum_data: continue
%>\


class ${class_name}(CtypesEnum):
%       for const, data in sorted(enum_data.items(), key=lambda x: x[1]['value']):
<%
            name = re.sub(pattern[0], pattern[1], const)
            if name[0].isdigit():
               name = '_' + name
%>\
    ${name} = ${data['value']}
%       endfor
%   endfor