<div align="center">

# Syntags: Write your markup in Python, easily

[Features] &emsp;•&emsp; [Install] &emsp;•&emsp; [License] &emsp;•&emsp; [Docs]

</div>

[Features]: #features
[Install]: #install
[License]: #license
[Docs]: https://github.com/SeparateRecords/Syntags/wiki

**Syntags** lets you generate HTML, XML, SVG, etc. by writing concise, _real_ Python code.

**Syntags** was built from the ground up for readable code. First-class support for _components_, _custom elements_, and _fragments_ is baked into the design.

**Syntags** takes a different approach to Pyxl — taking Python's own syntax and repurposing it, rather than using a custom character encoding and transforming your invalid code into valid code.

* The code you write is **real** Python, no magic.
* You don't need to learn the quirks of a new syntax.
* It's easy to get started with and integrate into your code.
* Highlighting works, and your linter will only be _slightly_ angry.

#### A brief note on the syntax ~

PEP 8 isn't gospel. Creating a beautiful syntax means ignoring certain parts of it, and that's okay! The second section, "[A Foolish Consistency is the Hobgoblin of Little Minds][consistency]," even summarises this.

<details>
<summary>View a relevant excerpt</summary>

> . . . **know when to be inconsistent** -- sometimes style guide
> recommendations just aren't applicable. When in doubt, use your best judgment.
> Look at other examples and **decide what looks best**.
>
> Some other good reasons to ignore a particular guideline:
>
> 1. When **applying the guideline would make the code less readable**, even for
>    someone who is used to reading code that follows this PEP.
>
> 2. . . .

</details>

Check out the [Syntags styleguide][styleguide] for recommendations on how to maintain good code quality.

[consistency]: https://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds

[styleguide]: https://github.com/SeparateRecords/Syntags/wiki/Styleguide

## Features

### an expressive syntax that _makes sense_

Structured like a programming language, because it _is_ one. No context switching between templating and programming.

```python
import syntags as tags
from syntags.html import *

app = html (lang="en") [
  head [
    title ["Some basic markup"]
  ],
  body [
    main [
      ...  # etc...
    ]
  ]
]

rendered = tags.render(app)
```

### intuitive syntax shorthands

It's effortless to write compact code that's easy to read and maintain.

```python
body [
  div .main_wrapper / main [
    ...
  ]
]

# The same, but without the shorthand:
body [
  div (classes={"main-wrapper"}) [
    main [
      ...
    ]
  ]
]
```

### reusable, declarative components

Similar to React, but very much Python.

```python
import syntags as tags
from syntags.html import *

@tags.component
def hello_message(name, **attrs):
  return div [
    f"Hello {name}"
  ]


rv = tags.render(hello_message (name="world"))
```

<details>
<summary>View the React JSX equivalent</summary>

```jsx
import React from "react";
import ReactDOMServer from "react-dom/server";

function HelloMessage({ name, ...props }) {
  return (
    <div>
      Hello {name}
    </div>
  );
}


rv = ReactDOMServer.renderToStaticMarkup(<HelloMessage name="world" />)
```

Keep in mind, this is in JSX. Compiling it is yet another step. Syntags' syntax is pure Python, no intermediate steps required.

</details>

### first-class fragments, no wizardry required

Fragments are just a sequence of elements, and they can be nested infinitely.

```python
HEAD_DATA = [
  link (rel="canonical", href="https://rob.ac/"),
  link (rel="stylesheet", href="dist/css/layout.css"),
  link (rel="shortcut icon", href="favicon.ico", type="image/x-icon")
]

html (lang="en") [
  head [
    HEAD_DATA
  ],
  ...
]
```

### simple, safe rendering

Everything becomes a string and gets escaped, except for raw strings.

```python
import syntags as tags
from syntags.html import *

rendered = tags.render(
  html (lang="en") [
    tags.raw("""
    <head>
      <title>A good example</title>
      <meta charset="UTF-8">
    </head>
    """),
    body [
      p [
        "<b>This will get escaped</b>"
      ]
    ]
  ]
)
```

### more than just HTML

Syntags comes with a bunch of namespaces to make your life easy.

* HTML tags: `html`
* XML prolog and tag factory: `xml`
* Some predefined XML namespaces: `svg`, `rss`, `sitemap`
* Common, useful components: `ext`

## Install

You can use Pip, or anything that can install from PyPI, such as [Poetry] or [Pipenv].

```console
$ pip install syntags
```

[Poetry]: https://python-poetry.org
[Pipenv]: https://pipenv.pypa.io/en/latest/

###### + Markdown component (`syntags.ext.markdown`)

```console
$ pip install syntags[markdown]
```

## License

Syntags is licensed under the ISC license, a simplified version of the MIT license. You can modify this project and use it in whatever you want! The only condition for redistribution is that you must include a copy of the license.

There's a copy in `syntags/__init__.py`, so you'll be fine as long as you don't remove that! Otherwise, you can include the copy found in the root of [the repository][repo].

[repo]: https://github.com/SeparateRecords/Syntags
