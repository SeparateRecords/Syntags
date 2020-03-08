# Syntags Styleguide

## Syntax

These intentional deviations from PEP 8 make the syntax more readable and
maintainable.

PEP 8 has a lot of rules to _visually_ bind symbols, to make it easier to follow
the code. Syntags uses these same symbols in a different way, so applying these
guidelines makes it harder to understand and change the code later.

### Tab length

**Recommendation:** Use 2 spaces for indentation. The interpreter is fine with
this as long as the indentation is consistent on a per-file basis. Most editors
will also infer tab size from the file.

Alternatively, use hard tabs and set the size however you like. You're the boss.

### Children

Keep a space between the element/component and the square brackets.

```python
# Good
parent [
  ...
]

# Bad - parent[ looks like one symbol
parent[
  ...
]
```

Avoid putting spaces around elements inline.

```python
# Good
parent [...]

# Ugly
parent [ ... ]
```

### Attributes

Have a space of padding between the attributes and the element/children.
Multi-line attributes follow the same rules.

```python
# Good
parent (k="v") [...]

# Bad - looks like a function
parent(k="v") [...]
```

If using a variable containing defaults, don't use `**kwargs` unpacking.
Instead, use the positional dictionary argument.

```python
attrs = {"class": "example test", "name": "foo"}

# Good
parent (attrs, name="bar")

# Bad - prone to TypeError (multiple values, invalid name)
parent (**attrs, name="bar")

```

### Classes

Put a space between the element name and classes.

```python
# Good
parent .large.yellow

# Bad - looks like accessing the "large" attribute
parent.large.yellow
```

Attributes go after classes.

```python
# Good
parent .example (k="v") [...]

# Bad - .large binds more closely to the () than the element
parent (k="v") .large [...]
```

### Single-child nesting

Always use spaces around the `/` operator.

```python
# Good
parent / child

# Bad - hard to distinguish the two elements
parent/child
```

### Fragments

Explicitly declared fragments should use square brackets, as it's consistent
with the element child syntax.

```python
# Good
frag = [
  ...,
]

# Bad - looks like element attributes
frag = (
  ...,
)
```

Fragments should not be unpacked using the `*args` syntax. Instead, they should
be treated like their own elements. This isn't a big deal in fragments, but it
can cause `SyntaxError`s in elements and components, so try to be consistent.

```python
x = [...]

# Good
y = [x, ...]

# Bad - more visual noise
y = [*x, ...]
```

### Functions and classes

Use whatever formatting you were already using for other objects, even inside a
tree of elements. This styleguide doesn't apply to the rest of your code, just
Syntags' special syntax!

```python
# Good
parent [
  child (prop="value"),
  isanswer(42)
]

# Bad - isanswer looks like a component, but it isn't one
parent [
  child (prop="value"),
  isanswer (42)
]
```

## Linting & Formatting Recommendations

Contributions are extremely welcome here! One person can only know so much about
so many programs.

Formatters mess with your code. Before trying to configure it to play a little
nicer, ask yourself - do you really *need* one? Most projects actually don't!

### Pylint

Until pylint supports `pylintrc` files in subdirectories, the best option is to
use something similar to the template below.

<details>
<summary>File: <code>pylintrc</code></summary>

```ini
[FORMAT]
# Fit more content (to make your files shorter) and black compatibility
max-line-length = 88


[TYPECHECK]
# @component returns a Component (different signature)
signature-mutators = component


[MESSAGES CONTROL]
# Shut up about the whitespace, etc.
disable =
  bad-whitespace,
  unused-wildcard-import,
  wildcard-import,
  missing-function-docstring,
  import-outside-toplevel,
  unused-argument
```

</details>

### Black

Black is very opinionated and has no configuration options for code style. Your
only choice is either disable for specific files, or sections of files using
explicit `# fmt: off` and `# fmt: on` comments. You can disable without
enabling.

### Yapf

Yapf allows you to disable formatting for particular expressions using
`# yapf: disable`.
