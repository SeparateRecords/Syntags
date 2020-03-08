"""RSS 2.0 tags.

See ``tagsext`` for useful components to simplify some boilerplate.

Tag names match their canonical web equivalents in casing unless they shadow a builtin,
in which case the first letter will be upper-cased.
"""

__all__ = [
    "author",
    "category",
    "channel",
    "cloud",
    "comments",
    "Copyright",
    "day",
    "description",
    "docs",
    "enclosure",
    "generator",
    "guid",
    "height",
    "hour",
    "image",
    "item",
    "language",
    "lastBuildDate",
    "link",
    "managingEditor",
    "name",
    "pubDate",
    "rating",
    "rss",
    "skipDays",
    "skipHours",
    "source",
    "textInput",
    "title",
    "ttl",
    "url",
    "webMaster",
    "width",
    "xml",
]

from syntags.lib.elements import xml_element
from syntags.xml import xml

author = xml_element("author")
category = xml_element("category")
channel = xml_element("channel")
cloud = xml_element("cloud")
comments = xml_element("comments")
Copyright = xml_element("copyright")
day = xml_element("day")
description = xml_element("description")
docs = xml_element("docs")
enclosure = xml_element("enclosure")
generator = xml_element("generator")
guid = xml_element("guid")
height = xml_element("height")
hour = xml_element("hour")
image = xml_element("image")
item = xml_element("item")
language = xml_element("language")
lastBuildDate = xml_element("lastBuildDate")
link = xml_element("link")
managingEditor = xml_element("managingEditor")
name = xml_element("name")
pubDate = xml_element("pubDate")
rating = xml_element("rating")
rss = xml_element("rss")
skipDays = xml_element("skipDays")
skipHours = xml_element("skipHours")
source = xml_element("source")
textInput = xml_element("textInput")
title = xml_element("title")
ttl = xml_element("ttl")
url = xml_element("url")
webMaster = xml_element("webMaster")
width = xml_element("width")
