<%
    from _metadata import attributes
%>\
# This file was generated
<%
    class_hierarchy = [
        ('TimeReference',           'object'),
        ('IEEE1588TimeReference',   'TimeReference'),
        ('IEEE8021ASTimeReference', 'TimeReference'),
        ('GPSTimeReference',        'TimeReference'),
        ('IRIGBTimeReference',      'TimeReference'),
        ('EtherCATTimeReference',   'TimeReference'),
        ('PPSTimeReference',        'TimeReference'),
# Do not generate port API
#        ('Port',                    'object'),
#        ('IEEE1588Port',            'Port'),
#        ('IEEE8021ASPort',          'Port')

    ]
%>\
%   for namespace, parent in class_hierarchy:


class ${namespace}(${parent}):
%       if parent == 'object':
    def __init__(self, session):
        self._session = session
%       endif
%       if namespace == 'TimeReference':
## Do not generate port API
##        self._ports = None

    @property
    def name(self):
        '''
        Returns the name of the time references instance.
        '''
        return self._session._active_item
## Do not generate port API
##    @property
##    def ports(self):
##        class PortSession(_SessionBase):
##            pass
##        if self._ports is None:
##            self._ports = []
##            num_ports = 1
##            tr_type = self._session.time_reference_type
##            if tr_type == 'IEEE 802.1AS-2011 TAB' or tr_type == 'IEEE 1588-2008 BC':
##                num_ports = 2
##            for _ in range(num_ports):
##                session = PortSession(self._session._vi, self._session._library, self._session._active_item)
##                if tr_type.startswith('IEEE 1588-2008'):
##                    self._ports.append(IEEE1588Port(session))
##                if tr_type.startswith('IEEE 802.1AS-2011'):
##                    self._ports.append(IEEE8021ASPort(session))
##        return self._ports
%       endif
<%
        additional_namespace_attrs = False
%>\
%       for _, attr in sorted(attributes.items()):
<%
        if attr['namespace'] != namespace:
            continue
        name = attr['short_name'].lower()
        additional_namespace_attrs = True
%>\

    @property
    def ${name}(self):
        return self._session.${attr['name'].lower()}

    @${name}.setter
    def ${name}(self, value):
        self._session.${attr['name'].lower()} = value
%       endfor
%       if not additional_namespace_attrs and parent != 'object':
    pass
%       endif
%   endfor
