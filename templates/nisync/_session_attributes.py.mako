<%
    from _metadata import attributes
    import re

    def to_snake_case(name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
%>\
# This file was generated

from nisync import _attributes


class SessionAttributes(object):
    """SessionAttributes class encapsulates specific attributes related to a session."""
%   for id, attr in sorted(attributes.items()):
<%
        if 'type' not in attr:
            continue

        name = attr['name'].lower()
%>\
    ${name} = _attributes.Attribute${attr['type']}(${id})
%   endfor
