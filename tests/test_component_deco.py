"""Test the @component decorator & co. work correctly."""

from dataclasses import dataclass

import pytest

from syntags.lib.components import Component, component, get_component_build_method


@dataclass
class MockComponent:
    children: tuple
    attrs: dict


class Expected(Exception):
    """Raised to indicate that the method was, indeed, called."""


def test_children_arg_detected():
    def func(children, **attrs):
        assert children == (True, True)
        assert attrs == {}
        raise Expected

    meth = get_component_build_method(func)
    instance = MockComponent((True, True), {})
    with pytest.raises(Expected):
        meth(instance)


def test_children_flattened():
    def func(children, **attrs):
        assert children == (True, True, True)

    meth = get_component_build_method(func)
    instance = MockComponent((True, (True, (True,))), {})
    meth(instance)
    assert instance.children != (True, True, True)


def test_attrs_no_children_if_arg_not_present():
    def func(**attrs):
        assert attrs == {}
        raise Expected

    meth = get_component_build_method(func)
    instance = MockComponent((True, True), {})
    with pytest.raises(Expected):
        meth(instance)


def test_first_pos_only_arg_is_children():
    def func(children, /, **attrs):
        assert children == ("abc",)
        assert attrs["children"] == ("xyz",)
        raise Expected

    meth = get_component_build_method(func)
    instance = MockComponent(("abc",), {"children": ("xyz",)})
    with pytest.raises(Expected):
        meth(instance)


def test_deco_creates_component_subclass():
    @component
    def example(**attrs):
        pass

    assert issubclass(example, Component)


def test_deco_copies_metadata():
    def control():
        pass

    @component
    def example(**attrs):
        """Docstring!"""

    assert example.__doc__ == "Docstring!"
    assert example.__module__ == control.__module__
    assert callable(example.build)


def test_deco_laziness():
    @component
    def example(**attrs):
        raise NotImplementedError

    example()
