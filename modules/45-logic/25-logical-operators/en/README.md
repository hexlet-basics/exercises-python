
We already know how to write functions that check single conditions. And in this lesson we will learn how to build compound conditions.

Suppose that the registration site requires that the password be longer than eight characters and contain at least one capital letter. Let's try to write two separate logical expressions and connect them with the special operator "AND":

> Password is longer than 8 characters **And** password contains at least one capital letter

Here is a function that takes the password and tells you whether it meets the conditions (`True`) or not (`False`):

```python
def has_capital_letter(str):
    # Checks the content of a capital letter in the string

 def is_correct_password(password):
    length = len(password)
    return length > 8 and has_capital_letter(password)

print(is_correct_password('Qwerty'))                   # => False
print(is_correct_password('Qwerty1234'))               # => True
print(is_correct_password('qwerty1234'))               # => False
```

`and` means "AND". In mathematical logic this is called a conjunction. The whole expression is true if every **operand** - each of the compound expressions - is true. In other words, `and` means both. The priority of this operator is lower than that of comparison operators. Therefore, the expression `has_capital_letter(password) and length > 8` works correctly without brackets.

In addition to `and`, the operator "OR" (disjunction) - is often used. It means "either or both". The expression `a or b` is true if at least one of the operands or all of them simultaneously are true. Otherwise, the expression is false.

Operators can be combined in any number and in any sequence. If `and` and `or` occur simultaneously in the code, the priority is given by parentheses. Below is an example of an extended function that determines the correctness of a password:

```python
def has_capital_letter(str):
    # Checks the content of a capital letter in the string

def has_special_chars(str):
    # Checks the content of special characters in the string

def is_strong_password(password):
    length = len(password)
    # The brackets set the priority. It is clear what relates to what.
    return (length > 8 and as_capital_letter(password)) and has_special_chars(password)
```

Now let's imagine that we want to buy an apartment that meets these conditions: an area of 100 square meters or more on any street **OR** an area of 80 square meters or more, but on Main Street.

Let's write a function that will check the apartment. It takes two arguments: the area is a number and the street name is a string:

```python
def is_good_apartment(area, street):
    return area >= 100 or (area >= 80 and street == 'Main Street')

print(is_good_apartment(91, 'Queens Street'))  # => False
print(is_good_apartment(78, 'Queens Street'))  # => False
print(is_good_apartment(70, 'Main Street'))    # => False

print(is_good_apartment(120, 'Queens Street'))  # => True
print(is_good_apartment(120, 'Main Street'))    # => True
print(is_good_apartment(80, 'Main Street'))     # => True
```

The area of mathematics in which logical operators are studied is called Boolean algebra. Below you will see **true tables** - you can use them to determine what the result will be if you apply the operator:

#### `and`

| A     | B     | A and B  |
| ----- | ----- | -------  |
| True  | True  | **True** |
| True  | False | False    |
| False | True  | False    |
| False | False | False    |

#### `or`

| A     | B     | A or B   |
| ----- | ----- | -------- |
| True  | True  | **True** |
| True  | False | **True** |
| False | True  | **True** |
| False | False | False    |
