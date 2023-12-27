
Look at the definition of the function that returns the modulus of the number passed:

```python
def abs(number):
    if number >= 0:
        return number
    return -number
```

But you can write it more succinctly. To do this, there must be an expression to the right of `return`, but `if` is an instruction, not an expression. In Python there is a construction that works like `if-else` but is considered an expression. It is called the **tern operator** - the only operator in Python that requires three operands:

```python
def abs(number):
    return number if number >= 0 else -number
```

The general pattern looks like this: `<expression on true> if <predicate> else <expression on false>'.

Let's rewrite the initial version of `get_type_of_sentence()` in the same way.

It was :

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    if last_char == '?':
        return 'question'
    return 'normal'
```

Became:

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    return 'question' if last_char == '?' else 'normal'

print(get_type_of_sentence('Hodor'))   # => normal
print(get_type_of_sentence('Hodor?'))  # => question
```

You can put a ternary operator into a ternary operator. But you shouldn't do it that way because such code is hard to read and debug.
