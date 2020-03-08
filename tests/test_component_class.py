"""Test the component class plumbing."""

import pytest

from syntags.lib.components import Component


def test_raises_if_not_overridden():
    with pytest.raises(NotImplementedError):
        Component().build()


def test_renders_build_method():
    class ComponentTest(Component):
        def build(self):
            return "test"

    assert str(ComponentTest) == "test"
