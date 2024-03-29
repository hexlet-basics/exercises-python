
The data we work with in programs have important attributes. In Python, they're built right into the language. Data also have methods - functions within properties. Properties and methods are expressions, just like variables or function calls. All of these can be combined in different ways. We'll look at the basics of them in this lesson.

In programming, we operate with data, create numbers and strings, perform various operations on them and use their results. To perform an operation, we apply either operators or functions:

```python
# Adding with the + operator
1 + 3 # 4

# Counting the length with the len() function
name = 'Hexlet'
len(name)  # 6
```

In the example above, there is a clear division: the data and functions are separated from each other. But this is not the only way to organize code. In Python, there's another approached used alongside this separation, the **Object Oriented (OO)** approach.

Object-oriented code is based on combining data and functions into one entity, an  **object**. Data in this case are called attributes, and functions are called methods.

This is what it looks like:

```python
name = 'Hexlet'
# upper() method
upper_name = name.upper()
print(upper_name)  # => 'HEXLET'
```

Strings in Python are objects. In the example above, we call a method, which is, a function associated with a string. The call is made using a period that comes right after the variable name. Otherwise, the methods work like normal functions.

The call can also be made directly:

```python
'Hexlet'.upper()  # 'HEXLET'
```

There are many methods built into strings which developers need all the time. You can see a list of them in the [documentation](https://python.readthedocs.io/en/latest/library/stdtypes.html#string-methods). Here are some useful examples:

```python
name = 'Python'

# Returns the index of the first occurrence of a letter in a string
name.find('t')  # 2

# Changes to lower case
name.lower()  # 'python'

# Replaces one substring with another
name.replace('on', 'off')  # 'Pythoff'
```

The same goes for numbers and other data types that we've not looked at. You could say that in Python almost everything is an object:

```python
x = -5
# Returns the modulus of a number
# The name looks strange, but it really is the name of the method
x.__abs__()
```

In the example above, there is a method name with two underscores at the beginning and at the end. In Python, this is the name given to methods that aren't intended to be called directly. Functions have been created for them that call methods themselves:

```python
x = -5
abs(x)  # calls x.__abs__()
# -5 to the power of 3
pow(x, 3)  # calls x.__pow__(3)
```

The creator of Python [decided](https://stackoverflow.com/questions/83983/why-isnt-the-len-function-inherited-by-dictionaries-and-lists-in-python) that it would be clearer if mathematical operations and operations similar to mathematic ones were expressed in functions. He wanted such functions to be thought of as operations like addition or subtraction. This is more familiar to those who have studied mathematics.

This is also how the `len()` function works:

```python
len('Hexlet')  # Calls 'Hexlet'.__len__()
```

In addition to methods, objects have attributes, but Python's built-in objects don't have many of them. For example, the attribute `__doc__`, which returns the documentation of the function. Therefore, functions are also considered objects:

```python
len.__doc__ # 'Return the number of items in a container.'
```

Attributes work and look like variables, only they need to be entered like this: `[object].[attribute]`.
