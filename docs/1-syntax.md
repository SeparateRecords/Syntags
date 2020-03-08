<div align="center">

# Syntags — An introduction to the syntax and tags

<h3>

**Introduction** &emsp;•&emsp; [Components] &emsp;•&emsp; [Styleguide]

[Components]: ./2-components.md
[Styleguide]: ./styleguide.md

</h3>

<details align="center">
<summary><b>Index</b></summary>
<br>

[**—— Basics ——**](#basics)

[Usage](#usage)

[Fragments](#fragments)

[Children](#children)

[Attributes](#attributes)

[**Example**](#example)

[**—— Shorthand ——**](#shorthand)

[Classes](#classes)

[Nesting](#nesting)

</details>
</div>
<hr>
<br>

The examples use a REPL-style format to show the output of rendering.

Every example assumes these imports.

```python
import syntags as tags
from syntags.html import *
```

<a name="usage"></a>

<h2 align="center">Basics</h2>

Elements exist in namespaces, and when you import them you can use them as-is. No extra parentheses!

```python
>>> tags.render(div)
'<div></div>'
>>> tags.render(br)
'<br>'
```

<details>
<summary>Included namespaces</summary>
<br>

* `html`
* `svg`
* `rss`
* `xml`
* `sitemap`
* `ext`

</details>

###### Fragments

A fragment is just a sequence. You can nest as many as you want.

```python
>>> frag = [
...   head,
...   body
... ]
...
>>> tags.render(frag)
'<head></head><body></body>'
>>> x = [br, br]
>>> y = [hr, x]
>>> tags.render(y)
'<hr><br><br>'
```

###### Children

Elements can take children by using square brackets. It's like assigning a fragment to a parent. Technically, that's actually what's happening!

```python
>>> doc = html [
...   head,
...   body
... ]
>>> tags.render(doc)
'<!DOCTYPE html><html><head></head><body></body></html>'
```

Strings are also valid children, but they'll be escaped unless you explicitly use a raw string.

```python
>>> string = "Some content, and some <dangerous characters>"
>>> tags.render(body [string])
'<body>Some content, and some &lt;dangerous characters&gt;</body>'
>>> tags.render(body [tags.raw(string)])
'<body>Some content, and some <dangerous characters></body>'
```

###### Attributes

Use parentheses to give an element some attributes. Keyword arguments will use aliases for reserved Python keywords, but a dictionary is treated as literal.

```python
>>> tag = a (href="https://example.com") [
...   "Click me"
... ]
...
>>> tags.render(tag)
'<a href="https://example.com">Click me</a>'
>>> scpt = script ({"async": True, "src": "example.js"})
>>> tags.render(scpt)
'<script async src="example.js"></script>'
```

<details>
<summary>Attribute rendering rules & aliases</summary>

* Keyword arguments are un-aliased.

  Keyword | Alias
  ------- | --------
  for     | for_id
  class   | classes
  async   | is_async

* All non-boolean values are converted to strings and escaped (unless they're raw values).

* Booleans display as just the key if `True`, and are not included if `False`.

  The code to render `<details open></details>` would be:

  ```python
  details (open=True)
  ```

  If `open` was set to `False`, it would render as `<details></details>`.

* Sequences are joined by spaces. Iterables (sequences _without_ an order) are sorted, then joined by spaces.

  Each of these objects will render identically.

  ```python
  >>> div ({"class": "a b"})

  >>> div (classes=["a". "b"])

  >>> div (classes={"b", "b", "a"})
  ```

</details>

<h2 align="center">Example</h2>

Let's build the basic structure that Emmet gives when you expand `!`.

For reference, the HTML is:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>

</body>
</html>
```

In Syntags, the `html` element gives you the doctype for free.

```python
import syntags as tags
from syntags.html import *

tree = html (lang="en") [
  head [
    meta (charset="UTF-8"),
    meta (name="viewport", content="width=device-width, initial-scale=1.0"),
    title ["Document"]
  ],
  body
]

exclamation = tags.render(tree)
```

<h2 align="center">Shorthand</h2>

Let's look at how you can do that stuff in fewer characters.

###### Classes

In CSS, you refer to a class using `.class`, or multiple as `.class.other`, etc. Elements use the same syntax to declare classes.

Underscores will be converted to dashes, and class names cannot start with underscores. Naturally, this conflicts with [BEM] naming. To use BEM, you'll need to use the `classes` keyword argument or `class` dict key.

[BEM]: https://getbem.com

```python
>>> image = div .image.large [
...   img .no_select (src="assets/img.jpg", alt="")
... ]
...
>>> tags.render(image)
'<div class="image large"><img class="no-select"></div>'
```

###### Nesting

If an element has only one child, _and that child is also an element_, you can use a slash `/` to nest them. This is called single-child nesting.

This saves you a level of indentation, and makes it easier to mentally bind the wrapper to the wrappee.

```python
body [
  div .article_wrapper / article [
    ...
  ]
]
```

The class example with the `img` tag is a good example of when *not* to use single child nesting. The line becomes messy and hard to visually parse.

```python
div .image.large / img .no_select (src="assets/img.jpg", alt="")
```

<details>
<summary>Behaviour and limitations</summary>

For context, a brief description of how the operator actually works:

1. `a / b` assigns `b` as a proxy to `a` (all future children are assigned to it).
2. It adds `b` as a child of `a`.
3. It returns `a`, which now has a child and proxy.

Because of this, using `a / "text"` would set `"text"` as a proxy of `a`, and a string can't take children. This could lead to errors down the road, so incorrect usage will eagerly raise `TypeError` to prevent more headaches later.

Instead of `a / "text"`, you can use explicit child assignment `a ["text"]`.

</summary>

## Code Style and Recommendations

Check out the [styleguide] document for recommendations on formatting and tooling.

[styleguide]: styleguide.md
