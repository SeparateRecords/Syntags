"""Test the @component decorator & co. work correctly."""

from dataclasses import dataclass

from syntags.lib.components import Component, component


@dataclass
class MockComponent:
    children: tuple
    attrs: dict


def test_creates_component_subclass():
    @component
    def example(**attrs):
        pass

    assert issubclass(example, Component)


def test_copies_metadata():
    def control():
        pass

    @component
    def example(**attrs):
        """Docstring!"""

    assert example.__doc__ == "Docstring!"
    assert example.__module__ == control.__module__
    assert callable(example.build)


def test_laziness():
    @component
    def example(**attrs):
        raise NotImplementedError

    example()
