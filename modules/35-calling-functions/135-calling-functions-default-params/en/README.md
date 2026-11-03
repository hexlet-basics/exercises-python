
Let's look at the `round()` function, which rounds the number passed to it:

```python
result = round(10.25, 0)  # 10.0
```

We passed two parameters to it:

- Number to be rounded
- Rounding accuracy

`0` means that the rounding will be to an integer value. More often than not, you need to round to a whole number, not to two, three, four etc. decimal places. So the creators of the `round` function made the second parameter **optional**: if you leave it out (its default value is `None`), the number is also rounded to an integer. Only the form of the result differs: with `0` it is `10.0`, and without the second argument it is `10`:

```python
result = round(10.25)  # 10
```

And if you need a different precision, you can pass a parameter:

```python
# rounding to one decimal place
result = round(10.25, 1)  # 10.2
```

In the signature of `round()`, the required parameter `number` comes before the optional parameter `ndigits`. Another function may have a different number of parameters and different default values.

## Reading a function's documentation

Documentation explains what data a function accepts and what result it returns. The signature at the start of a reference entry shows the function's name, parameters, and their order. The text below it explains the parameters and the function's behavior. We need both parts to prepare a call.

Consider the [reference entry for `round()`](https://docs.python.org/3/library/functions.html#round). It starts with the signature `round(number, ndigits=None)`. The names `number` and `ndigits` represent parameters. In a call, we supply concrete values in their places, such as `round(10.25, 1)`.

The table connects the parts of the signature to the arguments in that call.

| Part of the signature | Meaning | In the call `round(10.25, 1)` |
| --- | --- | --- |
| `round` | Function name | We call `round()` |
| `number` | Required parameter, the number to round | We pass `10.25` |
| `ndigits=None` | Optional parameter with the default value `None` | We pass `1` instead of using the default |

The `=` in `ndigits=None` indicates a default value. This notation tells us that we can omit the second argument. The text below the signature explains how the function uses `None`. For `round()`, omitting the second argument means rounding to an integer.

The description of the result starts below the signature. The reference entry for `round()` says that the function returns a number rounded to the specified number of places after the decimal point. It also explains that the result is an integer when `ndigits` is omitted. The signature shows a valid call, and the description explains its result.

We can check both cases in Python's interactive shell (REPL). The `>>>` symbols are the shell prompt; the lines below the calls show the results.

```console
>>> round(10.25, 1)
10.2
>>> round(10.25)
10
```

Here, the first call passes the precision `1` and returns `10.2`. The second uses the default value of `ndigits` and returns the integer `10`. This connects the signature, the documentation's explanation, and the result of running the code.

## Reference notation

A reference may use special symbols. They help us read the signature and are not passed to the function in a call.

| Reference notation | How to read it |
| --- | --- |
| `round(number, ndigits=None)` | `ndigits` has a default value, so its argument can be omitted |
| `round(number[, ndigits])` | Another way to mark an optional argument in a reference. The square brackets are not part of the call |
| `abs(number, /)` | The parameter before `/` receives its argument by position. The `/` is not another parameter |

For example, `abs(number, /)` describes a function with one parameter. The call `abs(-5)` passes the number `-5` and returns `5`. Neither the name `number` nor the `/` symbol is copied into that call.

When using a browser's translation feature, compare function names, parameters, and symbols in the signature with the original. Code uses the original names from the documentation. A translation of the word `number` can help explain the description, but the call still receives an actual value such as `10.25`.

## Working with an unfamiliar function

We read a reference entry to solve a task. For example, to round a price to one decimal place, we find the number and precision in the signature of `round()`, check the meaning of precision in the description, and try `round(10.25, 1)`. If the result matches the description, we can use that call in the program.

Another function will have its own parameters and rules. Its signature tells us which arguments to pass, the description explains the result and restrictions, and a small example lets us check our understanding.
