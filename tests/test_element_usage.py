"""Test element composition works as expected."""

from syntags.lib.elements import Element


class A(Element):
    _name = "a"


class B(Element):
    _name = "b"


class C(Element):
    _name = "c"
    _void_if_leaf = True


class D(Element):
    _name = "d"


def test_composition():
    # fmt: off
    tree = (
        A.root [
            B (src="assets/example") [
                C / D,
                C
            ]
        ]
    )

    assert str(tree) == (
      '<a class="root">'
        '<b src="assets/example">'
          "<c>"
            "<d></d>"
          "</c>"
          "<c>"
        "</b>"
      "</a>"
    )
