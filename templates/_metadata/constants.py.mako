<%include file="/includes/header.py.mako" args="addon_file='attributes_addon.py'"/>

<% from functools import reduce %>\
constants = {
%   for define in merged_defines:
<%
        if (not define.startswith('NISYNC_VAL_')) and (not define.startswith('NISYNC_LOGIC_')):
            continue
        name, value = define.split()
        name_replace_list = [
            ('NISYNC_VAL_',''),
            ('NISYNC_',''),
            ('1588','IEEE_1588'),
            ('8021AS','IEEE_8021AS'),
        ]
        name = reduce(lambda x, y: x.replace(*y), name_replace_list, name)
        if not value.startswith('"'):
            value = ''.join(c for c in value if (c.isdigit() or c == '-'))
%>\
    '${name}':
    {
        'value': ${value},
        'visibility': '${'private' if define in headers['internal.h'].defines else 'public'}',
    },
%   endfor
}

error_codes = [
<%
    import xml.etree.ElementTree as ET
    tree = ET.parse(errors_path)
    root = tree.getroot()
%>\
%   for error in root.findall('./descriptions/error'):
<%
        py_symbol = error.find('code').get('altSymbol')

        name_mapping = {
            'ALLOC':    'ALLOCATION',
            'INV':      'INVALID',
            'SRC':      'SOURCE',
            'DEST':     'DESTINATION',
            'ATTR':     'ATTRIBUTE',
            'NSUP':     'NOT_SUPPORTED',
            'TR':       'TIME_REFERENCE',
            'LIB':      'LIBRARY',
            'FAILURE':  'FAILED',
            'FAULT':    'FAILED',
            'CAL':      'CALIBRATION',
            'RSRC':     'RESOURCE',
            'HW':       'HARDWARE',
            'SW':       'SOFTWARE',
            'CLK':      'CLOCK',
            'ADJ':      'ADJUSTMENT',
            'TRIG':     'TRIGGER',
            'DUP':      'DUPLICATE',
        }

        move_to_back = ['INVALID', 'NOT_SUPPORTED']

        py_symbol = py_symbol.replace('CAL_','')
        py_symbol = py_symbol.replace('ALLOC','ALLOC_FAILED')
        py_symbol = py_symbol.split('_')
        py_symbol = list(map(lambda word: name_mapping.get(word, word), py_symbol))
        if py_symbol[0] in move_to_back:
            py_symbol.append(py_symbol[0])
            del py_symbol[0]
        py_symbol = '_'.join(py_symbol)
%>\
    {
        'alt_symbol': '${error.find('code').get('altSymbol')}',
        'py_symbol': '${py_symbol}',
        'code': ${error.find('code').get('code')},
        'comment': '${error.find('comment').text.strip()}',
        'symbol': '${error.find('code').get('symbol')}',
        'message': '${error.find('desc').text.strip()}',
    },
%   endfor
]