"""Test element factory produces correct components."""

from syntags.lib.elements import Element


def test_void_inheritance():
    # A is not void
    A = Element._new("A", void=False)
    assert A._void_if_leaf is False

    # B should be void, because A was
    B = A._new("B")
    assert B._void_if_leaf is False

    # C overrides A's voidness
    C = A._new("C", void=True)
    assert C._void_if_leaf is True

    # D should inherit from C
    D = C._new("D")
    assert D._void_if_leaf is True


def test_caching_same_voidness():
    assert Element._new("Example") is Element._new("Example")


def test_caching_different_voidness():
    assert Element._new("Example", void=False) is not Element._new("Example", void=True)
