"""Implements the <?xml?> prolog."""

__all__ = ["xml"]

from syntags.lib.elements import XMLElement


class xml(XMLElement):
    _rhs_template = ""
    _lhs_template = _void_template = "<?$name?>"
    _lhs_attr_template = _void_attr_template = "<?$name $attrs?>"
