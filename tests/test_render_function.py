"""Test render() creates correct output."""

from syntags.lib.utils import RawSentinel, render


def test_accepts_single_input():
    assert render("test") == "test"


def test_accepts_sequence_of_inputs():
    assert render(("a", "b")) == "ab"


def test_doesnt_escape_rawsentinel_subclasses():
    class RawString(str, RawSentinel):
        pass

    assert render(RawString('"test"<>')) == '"test"<>'


def test_escapes_strings():
    assert render('"test"<>') != '"test"<>'


def test_ignores_none():
    assert render(("test", (None, "ing", ..., "!"))) == "testing!"
