"""Write your markup in pure Python.

See the readme on GitHub for documentation, examples, and other information.

https://github.com/SeparateRecords/Syntags
"""

#
# Copyright (c) 2020, Robert "SeparateRecords" Cooper <me@rob.ac>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

__title__ = "syntags"
__version__ = "0.1.0"
__author__ = "Robert Cooper <me@rob.ac>"
__copyright__ = "Copyright 2020, Robert Cooper (SeparateRecords)"
__license__ = "ISC"
__all__ = (
    # ~~ Public API ~~ The intended interface for end users.
    "component",
    "element",
    "raw",
    "render",
    "render_to_file",
    # ~~ Tag Namespaces ~~ These aren't imported to avoid evaluating them.
    "html",
    "xml",
    "rss",
    "sitemap",
    "svg",
    "ext",
    # ~~ Raw API ~~ Exposes some of the inner workings of the API. For nerds.
    "RawStr",
    "Component",
    "Element",
    "ATTR_ALIASES",
    # ~~ API ABCs ~~ For even bigger nerds.
    "RawSentinel",
    "Syntax",
    "SyntaxMeta",
)

from syntags.lib.components import Component, component
from syntags.lib.elements import Element, XMLElement, element, xml_element
from syntags.lib.syntax import Syntax, SyntaxMeta
from syntags.lib.utils import (
    ATTR_ALIASES,
    RawStr,
    RawSentinel,
    raw,
    render,
    render_to_file,
)
