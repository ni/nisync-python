<%include file="/includes/header.py.mako" args="addon_file='attributes_addon.py'"/>
<%
    import re
    attr_regex = re.compile(r'(\w+)\s+\(NISYNC_ATTR_BASE \+ ([0-9]+)L\)\s*/?\*?\s?((?:Vi\w+)?)\s?.*')
    NISYNC_ATTR_BASE = 1150000

    class RegexLookUp(object):
        def __init__(self, regex_list):
            self._regex_list = regex_list
        def __getitem__(self, key):
            for regex, item in self._regex_list:
                match = re.match(regex, key)
                if match:
                    short_name = match.group(2)
                    name_prefix = {
                        'TIMEREF': 'TIME_REFERENCE',
                        '1588':    'IEEE_1588',
                        '8021AS':  'IEEE_8021AS',
                     }.get(match.group(1), match.group(1))

                    if name_prefix:
                        name = name_prefix + '_' + short_name
                    else:
                        name = short_name
                    return name, short_name, item
    lookup = RegexLookUp([
        ('NISYNC_ATTR_(TIMEREF)_(CLK_ADJ_OFFSET)',     '_Deprecated'),
        ('NISYNC_ATTR_(GPS)_(UTC_OFFSET)',             '_Deprecated'),
        ('NISYNC_ATTR_(IRIG)_(TAI_OFFSET)',            '_Deprecated'),
        ('NISYNC_ATTR_(TIMEREF)_(CORRECTION)',         'Session'),
        ('NISYNC_ATTR_(TIMEREF)_(SELECTED_TYPE)',      'Session'),
        ('NISYNC_ATTR_(TIMEREF)_(SELECTED_NAME)',      'Session'),
        ('NISYNC_ATTR_(TIMEREF)_(.*)',                 'TimeReference'),
        ('NISYNC_ATTR_1588_()(TIMESTAMP_BUFFER_SIZE)', 'Session'),
        ('NISYNC_ATTR_1588_()(AVAILABLE_TIMESTAMPS)',  'Session'),
        ('NISYNC_ATTR_1588_()(CLOCK_RESOLUTION)',      'Session'),
        ('NISYNC_ATTR_(1588)_(.*)',                    'IEEE1588TimeReference'),
        ('NISYNC_ATTR_(8021AS)_(.*)',                  'IEEE8021ASTimeReference'),
        ('NISYNC_ATTR_(GPS)_(.*)',                     'GPSTimeReference'),
        ('NISYNC_ATTR_(IRIG)_(.*)',                    'IRIGBTimeReference'),
        ('NISYNC_ATTR_(PPS)_(.*)',                     'PPSTimeReference'),
        ('NISYNC_ATTR_()(.*)',                         'Session'),
    ])
%>\

attributes = {
%   for define in merged_defines:
<%
        if (not define.startswith('NISYNC_ATTR_')) or define.startswith('NISYNC_ATTR_BASE'):
            continue

        ## Rename 1588 CLOCK_STATE to be PORT_STATE to better reflect its true meaning.
        if define.startswith('NISYNC_ATTR_1588_CLOCK_STATE'):
            define = define.replace('CLOCK_STATE ', 'PORT_STATE', 1)

        long_name, offset, type = attr_regex.match(define).groups()
        full_name = (long_name.replace('AVAIL_TIMESTAMPS',   'AVAILABLE_TIMESTAMPS')
                              .replace('CLK_RESOLUTION',     'CLOCK_RESOLUTION')
                              .replace('DDS_FREQ',           'DDS_FREQUENCY')
                              .replace('INTF_NUM',           'INTERFACE_NUMBER')
                              .replace('SERIAL_NUM',         'SERIAL_NUMBER')
                              .replace('TIMESTAMP_BUF_SIZE', 'TIMESTAMP_BUFFER_SIZE'))

        name, short_name, namespace = lookup[full_name]

        IEEE_8021AS_PORT_PROPS = ['NISYNC_ATTR_8021AS_PORT_STATE',
                                  'NISYNC_ATTR_8021AS_AS_CAPABLE',
                                  'NISYNC_ATTR_8021AS_LOG_SYNC_INTERVAL',
                                  'NISYNC_ATTR_8021AS_LOG_ANNOUNCE_INTERVAL',
                                  'NISYNC_ATTR_8021AS_INTERFACE_NAME',
                                  'NISYNC_ATTR_8021AS_NEIGHBOR_PROP_DELAY_THRESH']

        IEEE_1588_PORT_PROPS = ['NISYNC_ATTR_1588_LOG_SYNC_INTERVAL',
                                'NISYNC_ATTR_1588_INTERFACE_NAME',
                                'NISYNC_ATTR_1588_LOG_MIN_DELAY_REQ_INTERVAL',
                                'NISYNC_ATTR_1588_PEER_MEAN_PATH_DELAY',
                                'NISYNC_ATTR_1588_LOG_ANNOUNCE_INTERVAL',
                                'NISYNC_ATTR_1588_ANNOUNCE_RECEIPT_TIMEOUT',
                                'NISYNC_ATTR_1588_DELAY_MECHANISM',
                                'NISYNC_ATTR_1588_LOG_MIN_PDELAY_REQ_INTERVAL',
                                'NISYNC_ATTR_1588_VERSION_NUMBER',
                                'NISYNC_ATTR_1588_PORT_STATE']

        ## Override the namespace for port properties
        if full_name in IEEE_8021AS_PORT_PROPS:
            namespace = 'IEEE8021ASPort'
        if full_name in IEEE_1588_PORT_PROPS:
            namespace = 'IEEE1588Port'
%>\
    ${NISYNC_ATTR_BASE + int(offset)}: {
## FIXME(python_api): Figure out how to retrieve access
##        'access': 'read-write',
        'name': '${name}',
        'full_name': '${full_name}',
        'short_name': '${short_name}',
        'long_name': '${long_name}',
        'namespace': '${namespace}',
%       if type:
        'type': '${type}',
%       endif
        'visibility': '${'private' if define in headers['internal.h'].defines else 'public'}',
    },
%   endfor
}
