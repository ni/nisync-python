<%
    from _metadata import constants

    previous = ""
%>\
"""This module defines constants for trigger and clock terminal names."""

# This file was generated
% for name, data in constants.items():
<% if not isinstance(data["value"], str): continue %>\
% if name.endswith("0"):

% endif
${data["value"].upper()} = "${data["value"]}"
<% previous = name %>\
% endfor
