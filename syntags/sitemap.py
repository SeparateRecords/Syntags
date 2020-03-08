"""XML tags for the sitemap schema."""

__all__ = [
    "changefreq",
    "lastmod",
    "loc",
    "priority",
    "sitemap",
    "sitemapindex",
    "url",
    "urlset",
]

from syntags.lib.elements import xml_element
from syntags.lib.components import component
from syntags.ext import xml_prolog as xml

SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"


@component
def urlset(children, **attrs):
    """Create a <urlset> element with preceeding <?xml?> prolog."""
    return xml / xml_element("urlset")(attrs, xmlns=SITEMAP_NS)[children]


@component
def sitemapindex(children, **attrs):
    """Create a <sitemapindex> element with preceeding <?xml?> prolog."""
    return xml / xml_element("sitemapindex")(attrs, xmlns=SITEMAP_NS)[children]


changefreq = xml_element("changefreq")
lastmod = xml_element("lastmod")
loc = xml_element("loc")
priority = xml_element("priority")
sitemap = xml_element("sitemap")
url = xml_element("url")
