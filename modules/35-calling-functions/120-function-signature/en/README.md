
The `pow()` function calculates a number to a given power. It takes two parameters: **the number** and **the power**. If you call `pow()` without parameters, Python outputs the following: `"TypeError: pow expected at least 2 arguments, got 0. The interpreter tells you that the function expects two parameters and you called it without them.

The `pow()` function always has two mandatory parameters, so it cannot be called with any other number of parameters.

Moreover, the parameters of `pow()` can only be numbers. For example, if you pass a couple of lines into it, it will result in the following error: `"TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'"`. The result of a function call is also always a number.

Other functions can have different amounts and types of parameters. For example, there may be a function that takes three parameters: a number, a string, and another number.

To know these details about a particular function, you have to look at its **signature**. It defines the input parameters and their types, as well as the output parameter and its type. You can read about the `pow()` function in the [official Python documentation](https://docs.python.org/3/library/functions.html?highlight=pow#pow). Usually the documentation for a function looks like this:

```python
pow(x, y[, z])

Returns x to the power of y; if z is present, returns x to the power of y, modulus z
```

The first line here is the function signature. The function has two mandatory parameters, `x` and `y`. The optional parameter `z` is given in square brackets. Next, the purpose of the function is explained. The documentation lets you know how many arguments the function has and what type they are. It also describes what the function returns and what type the return value will be.
