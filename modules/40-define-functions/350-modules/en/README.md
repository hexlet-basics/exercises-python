A Python file with functions and constants is called a **module**. You can connect it to your program using the `import` keyword and use ready-made code instead of writing it yourself.

Python comes with a standard library — a set of modules included with the language. One of the most commonly used is `math`, which provides mathematical functions and constants.

## Importing a Module

The `import` command at the top of a file makes the module's contents available:

```python
import math

print(math.floor(3.7))  # => 3
print(math.ceil(3.2))   # => 4
```

After importing, you access functions through the module name and a dot. `math.ceil(3.2)` calls the `ceil` function from the `math` module.

## Functions in the math Module

`floor` rounds a number down to the nearest integer, `ceil` rounds it up:

```python
import math

print(math.floor(7.9))  # => 7
print(math.ceil(7.1))   # => 8
print(math.ceil(7.0))   # => 7
```

The difference matters when the number is not whole. `floor(7.9)` gives 7, not 8, because 7 is the nearest integer below.

## Importing Specific Names

When you only need part of a module, you can import specific names:

```python
from math import ceil, floor

print(ceil(3.2))   # => 4
print(floor(3.7))  # => 3
```

This lets you use `ceil` and `floor` directly, without the `math.` prefix. The result is the same as using `import math`.

## Using a Module Inside a Function

An imported module is available throughout the file, including inside function bodies:

```python
import math

def trips_needed(items: int, capacity: int) -> int:
    return math.ceil(items / capacity)

print(trips_needed(10, 3))  # => 4
```

The function `trips_needed` uses `math.ceil`. The `import math` line at the top of the file makes this possible.
