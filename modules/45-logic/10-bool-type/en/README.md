
In addition to arithmetic operations, there are also comparison operations in mathematics, such as `5 > 4` or `3 < 1`. They also exist in programming. For example, when we go to a website, the username and password are compared with those in the database. If they are, they let us in; they authenticate us. In this lesson, we'll get to know more about comparison operations.

Programming languages have adapted all mathematical comparison operations unchanged, except for the equality and inequality operators. In mathematics, we use the `=` sign, but in programming, this is quite rare.

In many languages, the symbol `=` is used to assign values to variables. That's why in Python, we use `==` for comparison.

List of comparison operations:

* `<`  — less than
* `<=` — less than or equal to
* `>`  — more than
* `>=` — greater than or equal to
* `==` — equal to
* `!=` — not equal to

These operations apply not only to numbers. For example, you can use the equality operator to compare strings: `password == text` is a comparison of the value of strings that are written in different variables.

A logical operation like `5 > 4` or `password == text` is an expression. Its result is the special value `True` or `False`. This is a new data type for us - `bool`.

```python
result = 5 > 4
print(result)  # => True
print('one' != 'one')  # => False
```

Along with strings (`str`) and integers and rational numbers, the **`bool` type** is one of Python's primitive data types.

Let's try to write a simple function that takes the age of a child as input and determines whether the child is a baby or not. Babies are defined as children under one year old:

```python
def is_infant(age):
    return age < 1

print(is_infant(3))  # => False
```

Any operation is an expression, so the only line of the function we write is “return the value that results from the comparison `age < 1`”. Depending on the argument passed, the comparison will be `True` or `False`, and `return` will return that result.

Now, perform the check on a child who's six months old:

```python
print(is_infant(0.5))  # => True
```

The result of the `True` operation. So the child is definitely a baby.
