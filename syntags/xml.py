"""Implements the <?xml?> prolog, exports function ``x`` to create XML elements.

Elements can be defined inline or bound to local names. ``x()`` uses
``functools.lru_cache()``, meaning ``x("example")`` will always return the same object.
Binding to local names may be helpful when defining a custom namespace.

Examples of the two methods are below.

    >>> tree = x("root") [
    ...     x("element") [
    ...         x("myThing"),
    ...         x("leafNode")
    ...     ]
    ... ]

    >>> root = x("root")
    >>> element = x("element")
    >>> myThing = x("myThing")
    >>> leafNode = x("leafNode")
    >>> tree = root [
    ...     element [
    ...         myThing,
    ...         leafNode
    ...     ]
    ... ]
"""

__all__ = ["xml", "x"]

from syntags.lib.elements import XMLElement, xml_element as x


class xml(XMLElement):
    _rhs_template = ""
    _lhs_template = _void_template = "<?$name?>"
    _lhs_attr_template = _void_attr_template = "<?$name $attrs?>"
