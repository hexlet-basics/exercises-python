
In this lesson, we'll take a look at the `max()` function and see how it works in Python.

Some functions are a little different in that they take a variable number of parameters. And we're not talking about default values. Check out this example:

```python
max(1, 10, 3)  # 10
```

In the above example, the `max()` function finds the maximum value among the passed parameters. To find out how many parameters can be passed to the input, you need to look at the [documentation](https://docs.python.org/3/library/functions.html?highlight=pow#max) этой функции. Там мы увидим такую конструкцию:

```python
max(arg1, arg2, *args[, key])
```

This means that `max()` takes two or more parameters as input:

```python
max(1, -3, 2, 3, 2)  # 3
```

If the function finds several parameters with the maximum value, then it'll return the very first one.
