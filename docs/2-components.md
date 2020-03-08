<div align="center">

# Components in Syntags

<h3>

[Introduction] &emsp;•&emsp; **Components** &emsp;•&emsp; [Styleguide]

[Introduction]: ./1-syntax.md
[Styleguide]: ./styleguide.md

</h3>

<details align="center">
<summary>Index</summary>
<br>

[Usage](#Usage)

[Optional or required attributes](#optional-and-required-attributes)

[Children](#children)

</details>
</div>
<hr>
<br>

All of these examples assume these imports.

```python
import syntags as tags
from syntags.html import *
```

<h2 align="center">Usage</h2>

Components use the exact same syntax as elements. You can use them literally anywhere you'd use an element.

The easiest way to create a component is to use the `component` decorator. This decorator takes a function with any parameters, and changes it into a component (class).

A component that takes `**attrs` will take any number of attributes. You can pass the `attrs` dict to something else, because elements and components can take a dictionary as their first argument.

```python
@tags.component
def home(**attrs):
  return a (attrs, href="/") ["Home"]
```

<h2 align="center">Optional and required attributes</h2>

You can use required and optional arguments with a component too.

**Optional:**

```python
@tags.component
def hello(name="world", **attrs):
  return h1 [f"Hello, {name}!"]

# <h1>Hello, world!</h1>
s = tags.render(hello)
```

**Required:**

```python
@tags.component
def hello(name, **attrs):
  return h1 [f"Hello, {name}!"]

# raises a TypeError because ``name`` wasn't given
s = tags.render(hello)
```

You can restrict the number of attributes a component takes by not using `**attrs`.

```python
@tags.component
def strict_img(src="", alt=""):
  return img (src=src, alt=alt)

# Raises a TypeError, unexpected argument
tags.render(strict_img (data_example="test"))
```

<h2 align="center">Children</h2>

The `children` parameter is special, since it will always be a fragment containing the component's children.

```python
@tags.component
def custom_article(children, **attrs):
  return article .custom.classes [
    div .article_inner [
      children
    ]
  ]

# Usage:
custom_article [
  h1 ["Article title"],
  p ["Very informative article, with useful information."],
  p ["This is probably more useful with markdown to HTML or something."]
]
```

`children` is flattened, so you can safely iterate over it. This example builds an unordered list (`ul`), and puts each child in its own list item (`li`). The component's attribute dictionary `attrs` is passed on to the list.

```python
@tags.component
def list_of(children, **attrs):
  return ul (attrs) [
    [li [child] for child in children]
  ]

# Usage:
list_of .hl_green [
  "Item 1",
  "Item 2",
  b ["Item 3"]
]
```

<details>
<summary>Using a <code>children</code> attribute</summary>

The `children` parameter is only special if there are no positional-only parameters.

```python
def example(kids, /, children, **attrs):
  ...
```

This makes the first argument before the `/` the fragment of children, leaving the `children` keyword free.

</details>

Attributes and children are only escaped when rendered.
