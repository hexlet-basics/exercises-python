Python programs almost always use code written by others. Reinventing mathematical functions, date handling, or network requests makes no sense — all of this is already available. Python uses packages to share and reuse code.

A package is a directory of Python files organized by topic. The Python standard library contains dozens of such packages, covering everything from mathematics to filesystem access.

## Importing a Package

To use code from a package, import it with the `import` keyword. Let's look at the `math` package:

```python
import math

print(math.sqrt(16))  # => 4.0
print(math.pi)        # => 3.141592653589793
```

After `import math`, everything in the package is available through dot notation: `math.sqrt`, `math.floor`, `math.pi`.

## Importing Specific Names

An alternative syntax lets you import only what you need:

```python
from math import sqrt, pi

print(sqrt(25))  # => 5.0
print(pi)        # => 3.141592653589793
```

Now `sqrt` and `pi` are available directly, without the `math.` prefix. The `import math` form makes the origin of the function explicit — that helps when reading unfamiliar code. The `from math import` form is convenient when you need a few specific functions and writing the prefix every time is tedious.

## Aliases

The `as` keyword lets you give an imported name an alias:

```python
from math import sqrt as sq

print(sq(9))  # => 3.0
```

An alias is useful when a name conflicts with an existing variable or is simply too long.

## Standard Library

Python ships with a rich set of built-in packages. A few commonly used ones:

- `math` — mathematical functions: `sqrt`, `hypot`, `floor`, `ceil`, `pi`
- `random` — random numbers: `randint`, `choice`, `shuffle`
- `datetime` — working with dates and times

```python
import random

print(random.randint(1, 6))                          # => random number from 1 to 6
print(random.choice(['rock', 'paper', 'scissors']))  # => random element
```

## Third-Party Packages

Beyond the standard library, thousands of packages are created by developers around the world. Install them with `pip`, Python's package manager:

```bash
pip install requests
```

After installation, imports work the same way as for built-in packages.
