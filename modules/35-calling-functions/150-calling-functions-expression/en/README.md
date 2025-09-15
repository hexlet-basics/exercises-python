
Let's continue to look at functions and their components. Today, it's time to look at expressions. Let's consider what it is and whether a function call can be mistaken for an expression.

An expression in programming returns a result that can be used. You probably already know a lot about expressions and the principles by which they're constructed. For example, mathematical operations like addition and subtraction, string operations like concatenation are all expressions:

```python
1 + 5 * 3
'He' + 'Let'
# Variables can be part of an expression
rate * 5
```

The peculiarity of expressions is that they return a result that can be used again: for example, they can be assigned to a variable or printed. This is what it looks like in the code:

```python
# Here the expression is 1 + 5
sum = 1 + 5
print(1 + 5)
```

But not everything in programming is an expression. The definition of a variable is an instruction, which means it cannot be part of an expression. In other words, this code will lead to an error:

```python
# Meaningless code that won't work
10 + sum = 1 + 5
```

Now let's see if a function call can be taken as an expression.

We know that functions return results, therefore they're expressions. This leads to a lot of interesting possibilities. For example, we can use a function call directly in mathematical operations. This is how we can get the last character index in a word:

```python
name = 'python'
# Indexes start with zero
# Function call and subtraction together!
last_index = len(name) - 1
print(last_index)  # => 5
```

This code has no new syntax. We have merely connected parts we already know, we're relying on their nature. We could go even further:

```python
print(len(name) - 1)  # => 5
```

All of this applies for any function, e.g., string functions:

```python
name = 'python'
# Interpolation is used
print(f'Last character: {name[len(name) - 1]}')
# 'Last character: n'
```

As you will see next, expressions can be combined to produce increasingly complex behavior in different places and in any way. The more you learn and practice Python, the better you will understand expressions. Over time, you'll learn how to connect the pieces of code to get the results you want.
