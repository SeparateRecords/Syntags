"""Implements utilities relied on by other modules in the package.

This file should not import anything locally, because that will probably lead to a
circular import.
"""

from __future__ import annotations

import collections.abc
from functools import singledispatch
from textwrap import dedent
from os import PathLike
from typing import Any, Optional, Sequence
from xml.sax.saxutils import escape, quoteattr as quote

ATTR_ALIASES = {"classes": "class", "for_id": "for", "is_async": "async"}


class RawSentinel:
    """Empty sentinel mixin to indicate a type should be treated as safe when str'd."""


class RawStr(str, RawSentinel):
    """String that will not be escaped when rendered."""


def raw(text) -> RawStr:
    """Dedent the text and make it raw."""
    string = str(text)
    dedented = dedent(string)
    stripped = dedented.strip()
    return RawStr(stripped)


def flatten(fragment: Sequence[Any]):
    """Flatten a fragment of any depth."""
    for node in fragment:
        if isinstance(node, Sequence) and not isinstance(node, str):
            # node is actually a fragment itself, flatten it!
            yield from flatten(node)
        else:
            yield node


def render(markup) -> str:
    """Convert any given markup to a string representation."""
    # Make sure iterating over markup will be correct
    if isinstance(markup, str) or not isinstance(markup, Sequence):
        markup = (markup,)

    sink = []
    for x in flatten(markup):
        # None is used to represent no content, and ... is for documentation.
        if x in (None, ...):
            continue

        # Anything subclassing RawSentinel should not be escaped.
        if isinstance(x, RawSentinel):
            sink.append(str(x))

        # Anything else should be escaped.
        else:
            sink.append(escape(str(x)))

    return "".join(sink)


def render_to_file(path: PathLike, markup) -> None:
    """Write rendered markup to a file."""

    with open(path, "w") as f:
        f.write(render(markup))


def render_attrs(attr_dict) -> str:
    """Render the dictionary to a valid HTML space-separated attribute list."""
    rendered = (render_attr(val, name) for name, val in attr_dict.items())
    return " ".join(s for s in rendered if s)


@singledispatch
def render_attr(val, name: str) -> Optional[str]:
    """Render an attribute based on its value.

    Dispatches to the appropriate function.
    """
    return f"{name}={quote(str(val))}"


# RawSentinel should always be literal, must be first.
@render_attr.register(RawSentinel)
def _(val, name):
    return f'{name}="{val}"'


@render_attr.register(str)
def _(val, name):
    return f"{name}={quote(val)}"


@render_attr.register(bool)
def _(val, name):
    return name if val else None


# see: https://bugs.python.org/issue34498
@render_attr.register(collections.abc.Sequence)
def _(val, name):
    joined = " ".join(str(x) for x in val)
    return f"{name}={quote(joined)}"


# see: https://bugs.python.org/issue34498
@render_attr.register(collections.abc.Iterable)
def _(val, name):
    as_strings = sorted(map(str, val))
    joined = " ".join(as_strings)
    escaped = quote(joined)
    return f"{name}={escaped}"


def make_repr(*info, **details) -> str:
    """Concatenate information into a readable repr."""
    items = (str(arg) for arg in (*info, details) if arg)
    return "<" + " ".join(items) + ">"
