"""Test elements render correctly."""

from syntags.lib.elements import Element


class E(Element):
    _void_if_leaf = False
    _name = "e"


class V(Element):
    _void_if_leaf = True
    _name = "v"


def test_lhs_with_no_attrs():
    assert E()._render_lhs() == "<e>"


def test_lhs_with_attrs():
    assert E(key="value")._render_lhs() == '<e key="value">'


def test_rhs():
    assert E()._render_rhs() == "</e>"


def test_void_with_no_attrs():
    assert E()._render_as_void() == "<e>"


def test_void_with_attrs():
    assert E(key="value")._render_as_void() == '<e key="value">'


def test_render_self_without_attrs():
    assert E()._render_self() == ("<e>", "</e>")


def test_render_self_with_attrs():
    assert E(key="value")._render_self() == ('<e key="value">', "</e>")


def test_void_render_self_without_attrs():
    assert V()._render_self() == ("<v>", "")


def test_void_render_self_with_attrs():
    assert V(key="value")._render_self() == ('<v key="value">', "")
