"""Test that the attribute renderer works correctly."""

import pytest

from syntags.lib.utils import render_attr, RawSentinel


class RawString(RawSentinel, str):
    ...


@pytest.mark.parametrize(
    "val, expected",
    (
        (True, "test"),  # Returns key name for True
        (False, None),  # Returns None if False
        ("Example", 'test="Example"'),  # Works normally
        ("<>&<>", 'test="&lt;&gt;&amp;&lt;&gt;"'),  # Escape normal strings
        (RawString("<>&<>"), 'test="<>&<>"'),  # Don't escape subclasses of RawSentinel
        ([3, 1, 2, 4], 'test="3 1 2 4"'),  # Doesn't sort a sequence
        ({3, 1, 2, 4}, 'test="1 2 3 4"'),  # Does sort an iterable
    ),
)
def test_render_attr(val, expected):
    assert render_attr(val, "test") == expected
