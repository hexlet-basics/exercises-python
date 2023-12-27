
Along with the logical operators **AND** and **OR**, there is also an operation called “**negation**” It changes the logical meaning to the opposite. In programming, negation corresponds to the unary operator `not`:

```python
not True   # False
not False  # True
```

For example, if there's a function that checks if a number is even, then you can use negation to check if a number is odd:

```python
def is_even(number):
    return number % 2 == 0

print(is_even(10))      # => True
print(not is_even(10))  # => False
```

In the example above, we added `not` to the left of the function call and got the opposite action.

Negation is a tool with which you can express intended rules in code without writing new functions.

If you write `not is_even(10)`, the code will still work:

```python
print(not not is_even(10))  # => True
```

In logic, double negation means positive:

```python
not not True   # True
not not False  # False

print(not not is_even(10))  # => True
print(not not is_even(11))  # => False
```

Now you know what the operators **AND**, **OR** and `not` mean. They allow you to specify compound conditions with two or more logical expressions.
