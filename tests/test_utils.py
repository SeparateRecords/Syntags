"""Test remaining utilities."""

from syntags.lib.utils import flatten


def test_flatten():
    to_flatten = [
        1,
        [[([([([(2,)],)],)],)], 3],
        (4,),
        [[[{5, 6}, [[[[[7], 8]]]]]]],
        9,
    ]
    assert list(flatten(to_flatten)) == [1, 2, 3, 4, {5, 6}, 7, 8, 9]
