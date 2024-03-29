
In programming, many functions and methods have parameters that are rarely changed. In such cases, these parameters are given default values that can be changed as needed. This reduces the amount of identical code. Let's see how it looks like in practice.

Let's look at an example:

```python
# The function of degree increase
# The second parameter has a default value of two
def pow(x, base=2):
    return x ** base

# Three to the second power (two is the default setting)
pow(3)  # 3 * 3 = 9
# Three to the Third Degree
pow(3, 3)  # 3 * 3 * 3 = 27
```

The default value looks like a normal assignment in the definition. It only works if the parameter is not passed.

Imagine that you didn't bring the parts for your car with you to the car service. Then the car mechanic will offer you to put the ones he has - the default ones.

The default value can be even when there is only one parameter:

```python
def my_print(text='nothing'):
  print(text)

my_print()  # => "nothing"
my_print("Hexlet")  # => "Hexlet"
```

There can be any number of parameters with default values:

```python
def f(a=5, b=10, c=100):
```

The default values have one limitation. They must go at the very end of the parameter list. From the syntax point of view, it is impossible to create a function with an optional parameter followed by a mandatory one:

```python
# Такой код завершится с ошибкой
def f(a=5, b=10, c=100, x):
# And such a
def f(a=5, b=10, x, c=100):

# This code will work
def f(x, a=5, b=10, c=100):

# This one will work, too.
def f(x, y, a=5, b=10, c=100):
```

Now you know how to work with the default values of the parameters. You can have them for several parameters, or for one parameter. And remember that the default values should be at the very end of the parameter list. This knowledge will help to reduce the amount of identical code.
