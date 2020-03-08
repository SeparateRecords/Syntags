"""Namespace for HTML tags.

Tag names match their canonical web equivalents in casing unless they shadow a builtin,
in which case the first letter will be upper-cased.
"""

__all__ = [
    "a",
    "abbr",
    "acronym",
    "address",
    "applet",
    "area",
    "article",
    "aside",
    "audio",
    "b",
    "base",
    "basefont",
    "bdi",
    "bdo",
    "big",
    "blockquote",
    "body",
    "br",
    "button",
    "canvas",
    "caption",
    "center",
    "cite",
    "code",
    "col",
    "colgroup",
    "command",
    "comment",
    "data",
    "datalist",
    "dd",
    "Del",
    "details",
    "dfn",
    "dialog",
    "Dir",
    "div",
    "dl",
    "dt",
    "em",
    "embed",
    "fieldset",
    "figcaption",
    "figure",
    "font",
    "footer",
    "form",
    "frame",
    "frameset",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "head",
    "header",
    "hgroup",
    "hr",
    "html",
    "i",
    "iframe",
    "img",
    "Input",
    "ins",
    "isindex",
    "kbd",
    "keygen",
    "label",
    "legend",
    "li",
    "link",
    "main",
    "Map",
    "mark",
    "menu",
    "menuitem",
    "meta",
    "meter",
    "nav",
    "nextid",
    "noframes",
    "noscript",
    "Object",
    "ol",
    "optgroup",
    "option",
    "output",
    "p",
    "param",
    "picture",
    "plaintext",
    "pre",
    "progress",
    "q",
    "rb",
    "rbc",
    "rp",
    "rt",
    "rtc",
    "ruby",
    "s",
    "samp",
    "script",
    "section",
    "select",
    "small",
    "source",
    "span",
    "strike",
    "strong",
    "style",
    "sub",
    "summary",
    "sup",
    "table",
    "tbody",
    "td",
    "template",
    "textarea",
    "tfoot",
    "th",
    "thead",
    "time",
    "title",
    "tr",
    "track",
    "tt",
    "u",
    "ul",
    "var",
    "video",
    "wbr",
    "xmp",
]

from syntags.lib.elements import element, Element

# List from:
#   http://w3c.github.io/elements-of-html/
#   https://www.w3.org/TR/2012/WD-html-markup-20121025/elements.html
# Void elements as seen in:
#   https://www.w3.org/TR/2011/WD-html-markup-20110405/syntax.html#syntax-elements
#   https://developer.mozilla.org/en-US/docs/Glossary/empty_element

a = element("a")
abbr = element("abbr")
acronym = element("acronym")
address = element("address")
applet = element("applet")
area = element("area", void=True)
article = element("article")
aside = element("aside")
audio = element("audio")
b = element("b")
base = element("base", void=True)
basefont = element("basefont", void=True)
bdi = element("bdi")
bdo = element("bdo")
big = element("big")
blockquote = element("blockquote")
body = element("body")
br = element("br", void=True)
button = element("button")
canvas = element("canvas")
caption = element("caption")
center = element("center")
cite = element("cite")
code = element("code")
col = element("col", void=True)
colgroup = element("colgroup")
command = element("command", void=True)
data = element("data")
datalist = element("datalist")
dd = element("dd")
Del = element("del", void=True)
details = element("details")
dfn = element("dfn")
dialog = element("dialog")
Dir = element("dir", void=True)
div = element("div")
dl = element("dl")
dt = element("dt")
em = element("em")
embed = element("embed", void=True)
fieldset = element("fieldset")
figcaption = element("figcaption")
figure = element("figure")
font = element("font")
footer = element("footer")
form = element("form")
frame = element("frame", void=True)
frameset = element("frameset")
h1 = element("h1")
h2 = element("h2")
h3 = element("h3")
h4 = element("h4")
h5 = element("h5")
h6 = element("h6")
head = element("head")
header = element("header")
hgroup = element("hgroup")
hr = element("hr", void=True)
i = element("i")
iframe = element("iframe")
img = element("img", void=True)
Input = element("input", void=True)
ins = element("ins")
isindex = element("isindex", void=True)
kbd = element("kbd")
keygen = element("keygen", void=True)
label = element("label")
legend = element("legend")
li = element("li")
link = element("link", void=True)
main = element("main")
Map = element("map", void=True)
mark = element("mark")
menu = element("menu")
menuitem = element("menuitem", void=True)
meta = element("meta", void=True)
meter = element("meter")
nav = element("nav")
nextid = element("nextid", void=True)
noframes = element("noframes")
noscript = element("noscript")
Object = element("object", void=True)
ol = element("ol")
optgroup = element("optgroup")
option = element("option")
output = element("output")
p = element("p")
param = element("param", void=True)
picture = element("picture")
plaintext = element("plaintext")
pre = element("pre")
progress = element("progress")
q = element("q")
rb = element("rb")
rbc = element("rbc")
rp = element("rp")
rt = element("rt")
rtc = element("rtc")
ruby = element("ruby")
s = element("s")
samp = element("samp")
script = element("script")
section = element("section")
select = element("select")
small = element("small")
source = element("source", void=True)
span = element("span")
strike = element("strike")
strong = element("strong")
style = element("style")
sub = element("sub")
summary = element("summary")
sup = element("sup")
table = element("table")
tbody = element("tbody")
td = element("td")
template = element("template")
textarea = element("textarea")
tfoot = element("tfoot")
th = element("th")
thead = element("thead")
time = element("time")
title = element("title")
tr = element("tr")
track = element("track", void=True)
tt = element("tt")
u = element("u")
ul = element("ul")
var = element("var")
video = element("video")
wbr = element("wbr", void=True)
xmp = element("xmp")


class html(Element):
    _name = "html"
    _lhs_template = "<!DOCTYPE $name><$name>"
    _lhs_attr_template = "<!DOCTYPE $name><$name $attrs>"


class comment(Element):
    _lhs_template = "<!-- "
    _lhs_attr_template = "<!-- "
    _rhs_template = " -->"
