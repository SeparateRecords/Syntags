"""Test syntax meta delegates to class instance methods."""

from syntags.lib.syntax import SyntaxMeta


def test_string():
    class Str(metaclass=SyntaxMeta):
        def __str__(self):
            return "True"

    assert str(Str) == "True"


def test_getattr():
    class GetAttr(metaclass=SyntaxMeta):
        def __getattr__(self, name):
            return True

    assert GetAttr.getting_attr is True


def test_truediv():
    class TrueDiv(metaclass=SyntaxMeta):
        def __truediv__(self, other):
            return True

    assert (TrueDiv / None) is True


def test_getitem():
    class GetItem(metaclass=SyntaxMeta):
        def __getitem__(self, others):
            return True

    assert GetItem[None] is True
