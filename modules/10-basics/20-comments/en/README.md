Almost all programming languages allow you to leave comments in your code. The interpreter ignores them — they exist only for people, to explain how the code works, mark places that need fixing, or remind yourself what to add later:

```python
# Delete the line below after the registration task is done
print(10)
```

Comments in Python start with the `#` sign and can appear anywhere in the program. Everything after `#` is ignored by the interpreter:

```text
  # comment      ──→  [ skipped by interpreter ]
  print('hello') ──→  [ executed → hello ]
  # another one  ──→  [ skipped by interpreter ]
```

A comment can take up an entire line. When one line isn't enough, use several:

```python
# The night is dark and
# full of terrors.
print('I am the King')
```

Or place it at the end of a line with code:

```python
print('I am the King') # For Lannisters!
```

Comments don't affect how the program runs, but they make code easier to understand — both for your future self and for teammates reading your code.

> A good rule of thumb: write code that's clear without comments, but when something needs explaining — comment it.

## Special comments: BEGIN and END

As you work through lessons, you'll sometimes see code that looks like this in the editor:

```python
# BEGIN

# END
```

`BEGIN` and `END` are ordinary comments that don't affect how the program runs. They mark the place where you should write your solution — between them:

```python
# BEGIN
<your solution here>
# END
```

The code outside the markers is part of the exercise setup and should be left untouched. In short: if you see `BEGIN` and `END`, write your code between them.
