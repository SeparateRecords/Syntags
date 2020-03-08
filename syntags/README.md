# Syntags' Project Structure

## File contents

* Any top-level file in this package should be a tag namespace, with the exception of `__init__.py` (obviously).

  Tag names match their web-equivalents in casing unless they shadow a builtin, in which case the first letter will be upper-cased. Eg. `<map>` → `Map`, `<set>` → `Set`

* `lib/utils.py` holds the utilities that don't rely on any thing defined elsewhere in the package. It is a bunch of reusable functions and classes. To prevent a recursive import, this file should never import anything local.

* `lib/syntax.py` contains the `Syntax` and `SyntaxMeta` classes. These classes define the syntax, which is used by `Element` and `Component` (although it's general enough to be used by anything else).

* `lib/elements.py` defines `Element`, `XMLElement`, and their factories. Element-related logic goes here.

* `lib/components.py` defines `Component` and `@component`. Component-related logic goes here.

## Typing

Syntags is intentionally partially typed. Because there's so much syntactical fuckery and *interesting* code to get it working, fully typing it is a mess and makes the code so much less readable, with no benefit.
