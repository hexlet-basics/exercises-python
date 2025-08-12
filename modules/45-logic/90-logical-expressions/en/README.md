
In this lesson we will learn the rules for transforming an argument and how to work with compound expressions and double negation.

## Rules of Conversion

Look at the example:

```python
print(0 or 1)
```

```bash
1
```

The way the **ORI** operator works is that its execution from left to right is interrupted and the result of the first argument that can be converted to `True` is returned. If there is no such argument, the last one, the right one, is returned.

Example with operator **AND**:

```python
print(0 and 1)
```

```text
0
```

The way the **AND** operator works is that its execution from left to right is interrupted and the result of the first argument, which can be converted to `False`, is returned. If there is no such argument, the last one - the right one - is returned.

There are two conversion rules in Python:

* `0`, `0.0`, ``'` and `None` are cast to `False`. These values are called **falsy**. This includes other data types that we will study in Hexslet
* Everything else is reduced to `True`.

These rules are used in development, for example, to define a default value:

```python
value = name or ''
# Examples
234 or '' # 234
'hexlet' or '' # 'hexlet'
None or '' # ''
```

If `name` takes one of the falsy values, the variable `value` will be assigned an empty string. In this case, in the following code we will be able to handle `value` as a string.

But there is a potential bug here. If `name` contains a falsy value, and the variable `value` can be assigned values like `0`, `False`, `None`, the code above will not work correctly:

```python
# The significance is actually there,
# but it is Falsy, so it is not selected on the OR condition
False or '' # ''
0 or '' # ''
None or '' # ''
```

## Compound expressions

If you combine logical expressions with each other, you can get some pretty interesting ways of solving problems with code.

Suppose we need to implement code in which a variable is written:

* String `yes` if the number is even
* String `no` if odd

This can be done by using the knowledge gained above:

```python
# even number
result = 10 % 2 == 0 and 'yes' or 'no' # 'yes'
# or print directly to the screen
print(10 % 2 == 0 and 'yes' or 'no') # => 'yes'
# odd number
print(11 % 2 == 0 and 'yes' or 'no') # => 'no'
```

These expressions work according to order and priority. The priority of assignment is the lowest, so it happens at the end. The priority of comparison `==` is higher than the priority of the logical operators `and` and `or`, so the comparison occurs earlier. Further the code is executed from left to right, because the priority of `and` is higher than the priority of `or`. Let's look at it step by step:

```python
# For an even
# 1 step
10 % 2 == 0 # True
# 2 step
True and 'yes' # The result is true
# The or check is done, but the right part is not executed, because it immediately returns 'yes'.

# For an odd
# 1 step
11 % 2 == 0 # False
# 2 step
False and 'yes' # The result is false.
# 3 step
False or 'no' # Selects and returns 'no'
```

The same scheme can be used with any expression at the beginning:

```python
print(somefunc() and 'yes' or 'no')
```

## Double Negation

Recall what the operation of negation looks like:

```python
answer = True
print(not answer)  # => False
```

With double negation, the final value is equal to the initial value:

```python
answer = True
print(not not answer)  # => True
```

The `not` operator always returns a Boolean value, regardless of the type of the passed argument, rather than replacing the value with the opposite. Therefore, a double negation will also return a boolean True/False.

```python
answer = 'python'
print(not answer) # => False
print(not not answer) # => True
```

## Selection error

Imagine that we need to check whether a value is equal to one or the other. For example, the variable `value` must contain one of two values: `first` or ``second`. Beginner developers sometimes write this expression this way:

```python
value == ('first' or 'second')
```

However, such a code will lead to the wrong result. It is necessary to remember the priority of operations. The first thing is to calculate everything specified in brackets - `'first' or ` second'`. If you execute this code in Replit, the output will be as follows:

```text
python
Python 3.8.2 (default, Apr 12 2020, 15:53:37)
>>> 'first' or 'second'
'first'
>>>
```

Now replace the original expression with a partially calculated one:

```python
value == 'first'
```

Not at all what we expected. Now let's go back to the beginning and write the test correctly:

```python
# It is not necessary to put parentheses,
# because the priority == is higher than the priority of or
value == 'first' or value == 'second'
```
