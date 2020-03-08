"""Defines the ``Component`` class and ``@component`` decorator."""

from __future__ import annotations

import inspect
from typing import Callable, Type, final

from syntags.lib.syntax import Syntax, SyntaxMeta
from syntags.lib.utils import render, make_repr, flatten


class ComponentMeta(SyntaxMeta):
    """Implements sound __repr__ for non-instantiated Components."""

    def __repr__(cls) -> str:
        return make_repr(cls.__name__, "component")


class Component(Syntax, metaclass=ComponentMeta):
    def __repr__(self) -> str:
        name = self.__class__.__name__
        kids = len(self.children)
        return make_repr(name, "element", children=kids, attrs=self.attrs)

    @final
    def _collapse(self) -> str:
        """Build this component and render the resulting markup."""
        return render(self.build())

    def build(self):
        """Build a tree of nodes."""
        raise NotImplementedError("Component subclasses must implement build()")


def get_component_build_method(builder: Callable) -> Callable:
    """Get a build method based on the signature of the builder callable."""
    params = inspect.signature(builder).parameters

    if next(iter(params.values())).kind == inspect.Parameter.POSITIONAL_ONLY:
        # The first argument is positional-only, so that's now the children.
        def build(self):
            kids = tuple(flatten(self.children))
            return builder(kids, **self.attrs)

    elif "children" in params:
        # The "children" argument is special if there's no positional-only
        # parameters.
        def build(self):
            kids = tuple(flatten(self.children))
            return builder(children=kids, **self.attrs)

    else:
        # None of the above exceptions are met, so call the builder with
        # attributes as keyword arguments.
        def build(self):
            return builder(**self.attrs)

    return build


def component(builder: Callable) -> Type[Component]:
    """Create a Component using the defined builder function."""

    # Use a generic name if builder is a lambda, otherwise use its name
    if builder.__name__ == "<lambda>":
        name = "<lambda component>"
    else:
        name = builder.__name__

    cls_dict = {
        "__module__": builder.__module__,
        "__doc__": builder.__doc__,
        "build": get_component_build_method(builder),
    }

    return type(name, (Component,), cls_dict)
