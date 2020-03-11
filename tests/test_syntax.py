"""Test Syntax plumbing."""

import pytest

from syntags.lib.syntax import Syntax

# pylint: disable=pointless-statement


def test_init_setting_attrs():
    instance = Syntax({"a": True, "b": False}, b=True, c=True)
    assert instance.attrs == {"a": True, "b": True, "c": True}


def test_call_setting_attrs():
    instance = Syntax()({"a": True, "b": False}, b=True, c=True)
    assert instance.attrs == {"a": True, "b": True, "c": True}


def test_multiple_dicts():
    instance = Syntax({"a": 1, "b": 0}, {"a": 0}, {"c": 0})
    assert instance.attrs == {"a": 0, "b": 0, "c": 0}


def test_merging_attrs():
    instance = Syntax({"a": True, "b": False}, b=True, c=True)
    assert instance.attrs == {"a": True, "b": True, "c": True}

    instance({"a": False}, c=False)
    assert instance.attrs == {"a": False, "b": True, "c": False}


def test_self_proxy():
    instance = Syntax()
    assert instance._proxy is instance


def test_setting_proxy():
    instance = Syntax()
    child = Syntax()
    x = instance._with_child(child)
    assert instance._proxy is child
    assert x is instance


def test_setting_children():
    instance = Syntax()

    assert instance.children == ()

    instance[None]
    assert instance.children == (None,)

    instance[None, None]
    assert instance.children == (None, None)


def test_add_class():
    instance = Syntax()

    instance.example.example.testing_this.Caps

    assert instance.attrs["class"] == {"example", "testing-this", "Caps"}


def test_str():
    instance = Syntax()

    with pytest.raises(NotImplementedError):
        str(instance)
