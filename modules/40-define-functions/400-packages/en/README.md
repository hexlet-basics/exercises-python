Python programs almost always use code written by others. Reinventing mathematical functions, date handling, or network requests makes no sense — all of this is already available. Python uses packages to share and reuse code.

A regular package is a directory containing an _\_\_init\_\_.py_ file and Python modules organized by topic. The _\_\_init\_\_.py_ file can be empty. A directory can hold any files; this file identifies it as a regular Python package. The standard library provides both individual modules and packages.

## Importing Modules and Packages

To use code from a package, import it with the `import` keyword. Let's look at the `math` module:

```python
import math

print(math.sqrt(16))  # => 4.0
print(math.pi)  # => 3.141592653589793
```

After `import math`, its names are available through dot notation: `math.sqrt`, `math.floor`, `math.pi`.

## Importing Specific Names

An alternative syntax lets you import only what you need:

```python
from math import sqrt, pi

print(sqrt(25))  # => 5.0
print(pi)  # => 3.141592653589793
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

Python ships with a rich set of modules and packages. A few commonly used modules:

- `math` — mathematical functions: `sqrt`, `hypot`, `floor`, `ceil`, `pi`
- `random` — random numbers: `randint`, `choice`, `shuffle`
- `datetime` — working with dates and times

```python
import random

print(random.randint(1, 6))  # => random number from 1 to 6
print(random.choice(["rock", "paper", "scissors"]))  # => random element
```

## Creating a Regular Package

A package groups related modules under one import path. A project with payment modules can have this structure.

```text
payments/
├── __init__.py
├── stripe.py
└── paypal.py
```

The _\_\_init\_\_.py_ file belongs to the package, while _stripe.py_ and _paypal.py_ are its modules. Importing `payments.stripe` gives access through `payments.stripe`; `from payments import stripe` binds the same module to the shorter name `stripe`. Importing `payments` executes _\_\_init\_\_.py_, which may define names available through the package. This file stays empty when no initialization code is needed.

Python also supports namespace packages, which can combine portions from several directories without _\_\_init\_\_.py_. The packages created in this lesson are regular packages and include that file in every package directory.

## Third-Party Packages

Beyond the standard library, thousands of packages are created by developers around the world. Install them with `pip`, Python's package manager:

```bash
pip install requests
```

After installation, imports work the same way as for built-in packages.
