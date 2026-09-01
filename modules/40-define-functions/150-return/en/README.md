In this lesson, we'll learn to write functions that **return values**. Such functions answer a question and hand back the result of their work, as if to say: "Here you go, I've done the counting".

For example, a function can return a string with processed text, or a number calculated from a formula. The returned value can be used further on. It gets saved in a variable, passed to another function, or printed on the screen.

To make a function hand back a result, it uses the special keyword `return`. It ends the function and specifies exactly what has to be returned.

Here is an example of a function that turns text into uppercase:

```python
def shout(name):
    return name.upper()
```

We call `shout()`, pass a name into it, and get back a string in uppercase. That string is the result of the function.

```python
result = shout("hexlet")
print(result)  # => HEXLET

result2 = shout("code-basics")
print(result2)  # => CODE-BASICS
```

Unlike `print()`, `return` doesn't print anything. It just returns a value. The decision about what to do with it is made by the calling code.

When the function `shout("hexlet")` is called, the expression `name.upper()` is evaluated first. It returns the string `"HEXLET"`. Then `return` hands that value outward, to the place the function was called from. In our case, the value is saved in the variable `result` and then printed on the screen with `print()`.

## Returning a calculated expression

Functions don't have to return a parameter as is. Usually `return` is given an **expression**, which is evaluated first, and only then is the result handed outward.

```python
def full_name(first, last):
    return first.capitalize() + " " + last.capitalize()
```

In this example we assemble a full name from a first name and a last name. First the `capitalize()` methods are called, then the strings are joined with `+`, and the finished string is returned.

```python
name = full_name("aria", "stark")
print(name)  # => Aria Stark
```

Here, in the line `return first.capitalize() + " " + last.capitalize()`, both method calls are executed first, then the space is added, and only then the result is passed as the return value.

## Multi-line functions

Sometimes the body of a function needs several steps before the result is ready. In such cases we write several lines of code and use `return` at the end to give back the final value.

For example, let's write a function that formats a name: it trims the spaces around the edges and turns all the letters into uppercase.

```python
def format_name(name):
    clean = name.strip()
    uppercased = clean.upper()
    return uppercased
```

First we remove the spaces with the `strip()` method, then convert to uppercase with `upper()`, and return the final value.

```python
print(format_name("  hexlet  "))  # => HEXLET
```

### Code after `return`

When Python reaches the `return` statement, the function stops executing. Everything written after it inside the function **will not be executed**:

```python
def example():
    return "done"
    print("this code will never run")
```

That's why `return` is always written at the end of the logic. There can be many such endings inside one function, though. We'll look at that in more detail when we get to conditional expressions.
