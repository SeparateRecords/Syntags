"""Namespace of SVG tags.

Tag names match their canonical web equivalents in casing unless they shadow a builtin,
in which case the first letter will be upper-cased.
"""

__all__ = [
    "a",
    "animate",
    "animateMotion",
    "animateTransform",
    "audio",
    "canvas",
    "circle",
    "clipPath",
    "defs",
    "desc",
    "discard",
    "ellipse",
    "feBlend",
    "feColorMatrix",
    "feComponentTransfer",
    "feComposite",
    "feConvolveMatrix",
    "feDiffuseLighting",
    "feDisplacementMap",
    "feDistantLight",
    "feDropShadow",
    "feFlood",
    "feFuncA",
    "feFuncB",
    "feFuncG",
    "feFuncR",
    "feGaussianBlur",
    "feImage",
    "feMerge",
    "feMergeNode",
    "feMorphology",
    "feOffset",
    "fePointLight",
    "feSpecularLighting",
    "feSpotLight",
    "feTile",
    "feTurbulence",
    "Filter",
    "foreignObject",
    "g",
    "iframe",
    "image",
    "line",
    "linearGradient",
    "marker",
    "mask",
    "metadata",
    "mpath",
    "path",
    "pattern",
    "polygon",
    "polyline",
    "radialGradient",
    "rect",
    "script",
    "Set",
    "stop",
    "style",
    "svg",
    "switch",
    "symbol",
    "text",
    "textPath",
    "title",
    "tspan",
    "unknown",
    "use",
    "video",
    "view",
]

from syntags.lib.elements import xml_element

# From:
#   https://www.w3.org/TR/SVG/eltindex.html

a = xml_element("a")
animate = xml_element("animate")
animateMotion = xml_element("animateMotion")
animateTransform = xml_element("animateTransform")
audio = xml_element("audio")
canvas = xml_element("canvas")
circle = xml_element("circle")
clipPath = xml_element("clipPath")
defs = xml_element("defs")
desc = xml_element("desc")
discard = xml_element("discard")
ellipse = xml_element("ellipse")
feBlend = xml_element("feBlend")
feColorMatrix = xml_element("feColorMatrix")
feComponentTransfer = xml_element("feComponentTransfer")
feComposite = xml_element("feComposite")
feConvolveMatrix = xml_element("feConvolveMatrix")
feDiffuseLighting = xml_element("feDiffuseLighting")
feDisplacementMap = xml_element("feDisplacementMap")
feDistantLight = xml_element("feDistantLight")
feDropShadow = xml_element("feDropShadow")
feFlood = xml_element("feFlood")
feFuncA = xml_element("feFuncA")
feFuncB = xml_element("feFuncB")
feFuncG = xml_element("feFuncG")
feFuncR = xml_element("feFuncR")
feGaussianBlur = xml_element("feGaussianBlur")
feImage = xml_element("feImage")
feMerge = xml_element("feMerge")
feMergeNode = xml_element("feMergeNode")
feMorphology = xml_element("feMorphology")
feOffset = xml_element("feOffset")
fePointLight = xml_element("fePointLight")
feSpecularLighting = xml_element("feSpecularLighting")
feSpotLight = xml_element("feSpotLight")
feTile = xml_element("feTile")
feTurbulence = xml_element("feTurbulence")
Filter = xml_element("filter")
foreignObject = xml_element("foreignObject")
g = xml_element("g")
iframe = xml_element("iframe")
image = xml_element("image")
line = xml_element("line")
linearGradient = xml_element("linearGradient")
marker = xml_element("marker")
mask = xml_element("mask")
metadata = xml_element("metadata")
mpath = xml_element("mpath")
path = xml_element("path")
pattern = xml_element("pattern")
polygon = xml_element("polygon")
polyline = xml_element("polyline")
radialGradient = xml_element("radialGradient")
rect = xml_element("rect")
script = xml_element("script")
Set = xml_element("set")
stop = xml_element("stop")
style = xml_element("style")
svg = xml_element("svg")
switch = xml_element("switch")
symbol = xml_element("symbol")
text = xml_element("text")
textPath = xml_element("textPath")
title = xml_element("title")
tspan = xml_element("tspan")
unknown = xml_element("unknown")
use = xml_element("use")
video = xml_element("video")
view = xml_element("view")
