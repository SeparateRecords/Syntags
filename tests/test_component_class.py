"""Test the component class plumbing."""

import pytest

from syntags.lib.components import Component


class WasCalled(Exception):
    pass


def test_raises_if_not_overridden():
    with pytest.raises(NotImplementedError):
        Component().build()


def test_str_calls_build_method():
    class ComponentTest(Component):
        def build(self):
            raise WasCalled

    with pytest.raises(WasCalled):
        str(ComponentTest)
