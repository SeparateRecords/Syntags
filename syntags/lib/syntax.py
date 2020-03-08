"""Defines the ``Syntax`` base class, implemented by Element and Component.

``Syntax`` purely implements the syntax and data structure. It has absolutely no
idea what it's used for.
"""

from __future__ import annotations

from functools import reduce
from typing import Any, Dict, Mapping, Optional, Sequence, TypeVar, Union, final

from syntags.lib.utils import ATTR_ALIASES, RawSentinel

T = TypeVar("T", bound="Syntax")


class SyntaxMeta(type, RawSentinel):
    """Component metaclass for implementing shorthand syntax on the type."""

    def __str__(cls) -> str:
        return cls().__str__()

    def __getattr__(cls, name: str) -> Syntax:
        return cls().__getattr__(name)

    def __truediv__(cls, other: Union[Syntax, SyntaxMeta]) -> Syntax:
        return cls().__truediv__(other)

    def __getitem__(cls, others: Any) -> Syntax:
        return cls().__getitem__(others)


class Syntax(RawSentinel, metaclass=SyntaxMeta):
    attrs: Dict[str, Any]
    children: Sequence[Any]

    _proxy: Syntax

    # ——— Setting attributes ———

    def __init__(self, *attr_dicts: Optional[Mapping[str, Any]], **attrs: Any):
        """Optionally set attrs using either a dict (literal) or keywords (aliased)."""
        self._proxy = self
        self.children = ()
        self.attrs = {}

        # all the logic is already in __call__, no need to repeat :)
        self(*attr_dicts, **attrs)

    def __call__(self: T, *attr_dicts: Optional[Mapping[str, Any]], **attrs: Any) -> T:
        """Merge new attributes with any previously set, using a dict or keywords."""

        # Must be first so it can be overridden by keyword args.
        # Most of the time, attr_dicts will be either 0 or 1 dict.
        attr_dict = reduce(lambda cum, cur: {**cum, **cur}, attr_dicts, {})
        self.attrs.update(attr_dict)

        # Use aliases and replace underscores with dashes so users rarely
        # need to use attr_dicts
        for key, value in attrs.items():
            unaliased = ATTR_ALIASES.get(key, key)
            dashed = unaliased.replace("_", "-")
            self.attrs[dashed] = value

        return self

    # ——— Setting a proxy child ———

    def _with_child(self: T, child: Union[Syntax, SyntaxMeta]) -> T:
        """Set a child node to use a proxy when adding future children."""
        if isinstance(child, SyntaxMeta):
            child = child()

        if not isinstance(child, Syntax):
            msg = "Combination is only valid between two Syntax subclasses, not with "
            msg += repr(type(child).__name__)
            raise TypeError(msg)

        self._around(child)
        self._proxy = child
        return self

    def __truediv__(self: T, child: Union[Syntax, SyntaxMeta]) -> T:
        return self._with_child(child)

    # ——— Adding children ———

    def _around(self: T, others: Any) -> T:
        """Add multiple children to this node."""
        # The proxy is normally ``self``, but is sometimes a child. This allows
        # combining nodes by giving new children to the proxy.
        if isinstance(others, str) or not isinstance(others, Sequence):
            self._proxy.children = (others,)
        else:
            self._proxy.children = others
        return self

    def __getitem__(self: T, others: Any) -> T:
        return self._around(others)

    # ——— Adding classes ———

    def _add_class(self: T, name: str) -> T:
        """Merge a new name with previously set names, or create a set with one name.

        Note that underscores will be replaced by dashes in the name. This conflicts
        with BEM naming -- use the ``classes`` keyword or ``class`` dict key.
        """
        if name.startswith("_"):
            return self

        fixed_format = name.replace("_", "-")

        classes = self.attrs.setdefault("class", set())

        if isinstance(classes, str):
            # Splits on spaces to create a set, ensures unique classes
            self.attrs["class"] = {*classes.split(), fixed_format}
        else:
            classes.add(fixed_format)

        return self

    def __getattr__(self: T, name: str) -> T:
        return self._add_class(name)

    # ——— Rendering logic ———

    def _collapse(self) -> str:
        """Create a human-friendly string representation."""
        raise NotImplementedError("Syntax subclasses must implement _collapse()")

    @final
    def __str__(self) -> str:
        return self._collapse()

    # ——— Equality & Comparison ———

    def __eq__(self, other) -> bool:
        return self.__class__ is other.__class__ and self.attrs == other.attrs
