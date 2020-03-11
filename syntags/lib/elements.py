"""Defines most of the public interface for Syntags.

Attributes on ``Element`` and ``Component`` all start with underscores. This keeps
more names free to be used by the HTML class syntax.
"""

from __future__ import annotations

from functools import lru_cache
from string import Template
from typing import ClassVar, Optional, Tuple, TypeVar

from syntags.lib.syntax import Syntax, SyntaxMeta
from syntags.lib.utils import make_repr, render, render_attrs

T = TypeVar("T")


class ElementMeta(SyntaxMeta):
    """Implements __repr__ for non-instantiated Elements."""

    def __repr__(cls) -> str:
        return make_repr(cls()._name, "element")


class Element(Syntax, metaclass=ElementMeta):
    """A Syntax type that can render itself."""

    _name: str

    # If there are no children, should the tag render as a void tag?
    _void_if_leaf: ClassVar[bool] = False

    _lhs_template: ClassVar[str] = "<$name>"
    _lhs_attr_template: ClassVar[str] = "<$name $attrs>"
    _void_template: ClassVar[str] = "<$name>"
    _void_attr_template: ClassVar[str] = "<$name $attrs>"
    _rhs_template: ClassVar[str] = "</$name>"

    @classmethod
    @lru_cache(None)
    def _new(cls: T, name: str, *, void: Optional[bool] = None) -> T:
        """Create a subclass of this class using the given name."""

        is_void = {} if void is None else {"_void_if_leaf": void}
        cls_dict = {"_name": name, **is_void}
        return type(name, (cls,), cls_dict)

    @property
    def _name(self) -> str:
        """Get the name used in template substitution."""
        return self.__class__.__name__

    def _render_lhs(self) -> str:
        """Render the left side of the tag, with attributes if present."""
        if not self.attrs:
            lhs = Template(self._lhs_template)
            return lhs.safe_substitute(name=self._name)

        lhs = Template(self._lhs_attr_template)
        attrs = render_attrs(self.attrs)
        return lhs.safe_substitute(name=self._name, attrs=attrs)

    def _render_rhs(self) -> str:
        """Render the closing tag."""
        rhs = Template(self._rhs_template)
        return rhs.safe_substitute(name=self._name)

    def _render_as_void(self) -> str:
        """Render the complete tag, with attributes if present.

        This method is only called if both ``self._void_if_leaf == True`` and
        there are no children, otherwise the tag is rendered normally.
        """
        if not self.attrs:
            void = Template(self._void_template)
            return void.safe_substitute(name=self._name)

        void = Template(self._void_attr_template)
        attrs = render_attrs(self.attrs)
        return void.safe_substitute(name=self._name, attrs=attrs)

    def _render_self(self) -> Tuple[str, str]:
        """Render the entire tag, split into open and close strings.

        If the tag is void and has no children, the void tag and an empty string will
        be returned instead of the open and close tags.
        """
        if self._void_if_leaf and not self.children:
            return self._render_as_void(), ""

        return self._render_lhs(), self._render_rhs()

    def _render_children(self) -> str:
        """Render each child of this element."""
        return render(self.children)

    def __str__(self) -> str:
        """Collapse the element and all its children to a string."""
        lhs, rhs = self._render_self()

        kids = self._render_children()

        return f"{lhs}{kids}{rhs}"

    def __repr__(self) -> str:
        kids = len(self.children)
        return make_repr(self._name, "element", children=kids, attrs=self.attrs)


class XMLElement(Element):
    """Subclass of Element with correct XML semantics."""

    _void_if_leaf = True

    _void_template = "<$name />"
    _void_attr_template = "<$name $attrs />"


element = Element._new

xml_element = XMLElement._new
