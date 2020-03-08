"""Various components that provide non-standard functionality.

These components simplify common repetitive/verbose elements, such as adding CSS,
fonts from Google Fonts, or elements that can only ever have -- and must contain -- one
child (looking at <rss> 👀).

Components import their own dependencies. This avoids evaluating each namespace
when this file is imported.
"""

__all__ = ["comment", "css", "google_fonts", "xml_prolog", "rss_channel", "markdown"]

from syntags.lib.components import component
from syntags.lib.utils import RawStr, render


# fmt: off

@component
def comment(children):
    """Create a comment, escaping any end-sequences."""
    rendered = render(children)
    safe = rendered.replace('-->', '--&gt;')
    return RawStr(f"<!-- {safe} -->")


@component
def css(**attrs):
    """Build a link containing the expected rel and type attributes."""
    from syntags.html import link

    return link (attrs, rel="stylesheet", type="text/css")


@component
def google_fonts(fonts, **attrs):
    """Build a link with the correct Google Fonts URL.

    Must use the ``fonts`` attribute with an iterable (list, set, etc).

        >>> google_fonts (fonts={"Roboto", "Roboto Slab:600,700"})

    Additional attributes will be passed to the created ``link`` element.
    """
    base_url = "https://fonts.googleapis.com/css?display=swap&family="
    formatted = "|".join(fonts).replace(" ", "+")
    fonts_url = base_url + formatted
    return css (attrs, href=fonts_url)


@component
def xml_prolog(children, **attrs):
    """Create an XML prolog with UTF-8 encoding and the version set to 1.0.

        >>> from syntags.xml import x
        >>> from syntags.ext import xml_prolog
        >>> xml_prolog / x("root") [
        ...     x("my-element") [
        ...         "example"
        ...     ]
        ... ]
    """
    from syntags.xml import xml

    return xml (attrs, version="1.0", encoding="UTF-8") [children]


@component
def rss_channel(children, **attrs):
    """Create a channel, with RSS 2.0 tag and XML 1.0 prolog.

        >>> from syntags.rss import *
        >>> from syntags.ext import rss_channel
        >>> rss_channel [
        ...     title ["A good example"],
        ...     author ["SeparateRecords"],
        ...     ...
        ... ]
    """
    from syntags.rss import rss, channel

    return xml_prolog / rss (attrs, version="2.0") / channel [children]


@component
def markdown(children, extras=None, src=None, **attrs):
    """Render some markdown to a raw HTML string.

    This component uses markdown2 for rendering. It enables the
    fenced-code-blocks and header-ids extras, and allows you to add more with
    the ``extras`` attribute (list).

    See the following link for a list of the supported extras:
    https://github.com/trentm/python-markdown2/wiki/Extras#implemented-extras

    You can render a file.

        >>> markdown (src="posts/1.md")

    Or some inline markdown.

        >>> markdown [
        ...     '''
        ...     # Title
        ...
        ...     Content
        ...     '''
        ... ]

    Or both, using the ellipsis literal as a placeholder.

        >>> markdown (src="docs/1-syntax.md") [
        ...     ...,
        ...     '''
        ...
        ...     ## Style Recommendations
        ...
        ...     See the [styleguide] for recommendations on how to keep your
        ...     code readable and maintainable in the long term, and configuration
        ...     for your linter.
        ...
        ...     '''
        ... ]

    This component requires the "markdown" extra.

        $ pip install syntags[markdown]

    """
    import textwrap

    try:
        import markdown2 as md
    except ImportError as e:
        raise ImportError("Syntags: Missing feature 'markdown'") from e

    # Add some sensible extras to control how the markdown renders.
    md_extras = ["fenced-code-blocks", "header-ids"]
    if extras:
        md_extras += extras

    # Only render path to markdown if it's actually needed.
    rendered_src = ""

    if src and (not children or ... in children):
        rendered_src = md.markdown_path(src, extras=md_extras)

    if not children:
        return RawStr(rendered_src)

    # Each item is a sequence of uninterrupted, non-ellipsis children that
    # have been joined by newlines.
    joined_md = []

    # Collects children until an ellipsis is found and they get moved to
    # ``joined_md``
    sink = []
    for child in children:
        if child is not ...:
            as_string = str(child)
            dedented = textwrap.dedent(as_string)
            stripped = dedented.strip()
            sink.append(stripped)
        else:  # child is ...
            joined_md.append("\n".join(sink))
            sink.clear()

    # There's still stuff in the sink if there was no ellipsis
    joined_md.append("\n".join(sink))

    rendered = [md.markdown(item, extras=md_extras) for item in joined_md]
    final_markdown = rendered_src.join(rendered)

    return RawStr(final_markdown)
