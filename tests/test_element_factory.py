"""Test element factory produces correct components."""

from syntags.lib.elements import Element, get_element_factory as new


def test_void_inheritance():
    # A is not void
    A = new(Element)("A", void=False)
    assert A._void_if_leaf is False

    # B should be void, because A was
    B = new(A)("B")
    assert B._void_if_leaf is False

    # C overrides A's voidness
    C = new(A)("C", void=True)
    assert C._void_if_leaf is True

    # D should inherit from C
    D = new(C)("D")
    assert D._void_if_leaf is True


def test_caching_same_voidness():
    assert new(Element)("Example") is new(Element)("Example")


def test_caching_different_voidness():
    assert new(Element)("Example", void=False) is not new(Element)("Example", void=True)
