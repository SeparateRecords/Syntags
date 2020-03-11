"""Defines the ``Component`` class and ``@component`` decorator."""

from __future__ import annotations

import inspect
from typing import Callable, Type, final

from syntags.lib.syntax import Syntax, SyntaxMeta
from syntags.lib.utils import flatten, make_repr, render


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
    def __str__(self) -> str:
        """Build this component and render the resulting markup."""
        return render(self.build())

    def build(self):
        """Make the component build some markup."""
        raise NotImplementedError("Component subclasses must implement build()")


def get_component_build_method(builder: Callable) -> Callable:
    """Get a valid build() method based on the signature of builder function."""
    params = inspect.signature(builder).parameters

    # If the first argument is positional-only, that should be the children.
    # next() will raise StopIteration if params is empty, check first.
    if params and next(iter(params.values())).kind == inspect.Parameter.POSITIONAL_ONLY:

        def build(self):
            kids = tuple(flatten(self.children))
            return builder(kids, **self.attrs)

    # The "children" parameter is special if there's no positional-only
    # params.
    elif "children" in params:

        def build(self):
            kids = tuple(flatten(self.children))
            return builder(children=kids, **self.attrs)

    # None of the above exceptions are met, so call the builder with
    # attributes as keyword arguments.
    else:

        def build(self):
            return builder(**self.attrs)

    return build


def component(builder: Callable) -> Type[Component]:
    """Create a Component using the builder function."""

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
