
An operation character, such as `+`, is called an **operator**. Operators perform operations on certain values, which are called **operands**. The operators themselves are usually one or more characters. On occasion it can also be a word. Most of the operators are identical to those you'll have seen in math class.

```python
print(8 + 2)
```

In this example `+` — s the operator, and the numbers `8` and `2` — are **operands**.

When we add up, we have two operands: one to the left of the `+` sign, and one to the right. Operations that require two operands are called **binary**. operations. If at least one operand is omitted, e.g., `3 +`, the program will end with a syntax error.

Operations can be more than just binary, they can also be unary (one operand), and ternary (three operands). Moreover, operators may look the same but denote different operations.  The symbols `+` and `-` are not only used as operators. When it comes to negative numbers, the minus sign becomes part of the number:

```python
print(-3)  # => -3
```

Above is an example of applying a unary operation to the number `3`. The minus operator before the three tells the interpreter to take the number `3` and find the opposite, i.e., `-3`. This can be confusing because `-3` is both a number in itself and an operator with an operand. But this is the structure programming languages have.
