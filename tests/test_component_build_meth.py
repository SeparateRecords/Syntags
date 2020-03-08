import pytest

from dataclasses import dataclass

from syntags.lib.components import Component, component, get_component_build_method


class WasCalled(Exception):
    """Raised to indicate that the method was, indeed, called."""


@dataclass
class MockComponent:
    children: tuple
    attrs: dict


def test_func_with_no_params_raises_error_if_given_arguments():
    def func():
        pass

    meth = get_component_build_method(func)
    instance = MockComponent((), {"xyz": "abc"})

    with pytest.raises(TypeError):
        meth(instance)


def test_children_param_is_instance_children():
    def func(children, **attrs):
        assert children == (1, 1)
        assert attrs == {}
        raise WasCalled

    meth = get_component_build_method(func)
    instance = MockComponent((1, 1), {})

    with pytest.raises(WasCalled):
        meth(instance)


def test_children_is_flattened():
    def func(children, **attrs):
        assert children == (1, 1, 1)
        raise WasCalled

    meth = get_component_build_method(func)
    instance = MockComponent((1, (1, (1,))), {})

    # The actual instance's children shouldn't be flattened eagerly.
    assert instance.children != (1, 1, 1)

    with pytest.raises(WasCalled):
        meth(instance)


def test_no_children_key_in_attrs_if_children_param_not_present():
    def func(**attrs):
        assert attrs == {}
        raise WasCalled

    meth = get_component_build_method(func)
    instance = MockComponent((None,), {})

    assert instance.children != ()
    with pytest.raises(WasCalled):
        meth(instance)


def test_first_pos_only_arg_is_children():
    def func(kids, /, children, **attrs):
        assert kids == ("abc",)
        assert children == ("xyz",)
        raise WasCalled

    meth = get_component_build_method(func)
    instance = MockComponent(("abc",), {"children": ("xyz",)})

    with pytest.raises(WasCalled):
        meth(instance)
