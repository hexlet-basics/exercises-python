Comparison operations work with numbers and with strings. In Python strings are compared lexicographically: character by character, left to right, by the numeric codes of the characters (Unicode).

```python
print("apple" < "banana")  # => True
print("cat" > "dog")  # => False
print("abc" == "abc")  # => True
print("hello" != "world")  # => True
```

Here `"apple" < "banana"` because the code of `a` (97) is smaller than the code of `b` (98), and it is the first character that decides the outcome of the comparison. The code of a character can be seen like this: `ord('a')` → `97`.

```python
print(ord("a"))  # => 97
print(ord("b"))  # => 98
```

The comparison is case-sensitive: `'Z'` (90) < `'a'` (97). An example of a comparison where the first letters are of different case:

```python
print("Zebra" < "apple")  # True — 'Z'(90) < 'a'(97)
print("apple" < "Banana")  # False — 'a'(97) > 'B'(66)
print("Apple" < "apple")  # True  —  'A'(65) < 'a'(97)
```

Let's write a function that checks whether a word starts with a given letter. To do that we take the first character of the string and compare it with the needed letter.

```python
def starts_with(word: str, letter: str) -> bool:
    return word[0] == letter


print(starts_with("apple", "a"))  # => True
print(starts_with("banana", "a"))  # => False
```

Comparison operations are expressions just like arithmetic ones. Ready values and other expressions can be substituted into them, as in the example above: `word[0]`. For example, instead of a number you can use the result of the function `len`, which returns the length of a string:

```python
print(len("apple") > 3)  # => True, because len("apple") = 5
print(len("hi") > 3)  # => False, because len("hi") = 2
```

In the example above, the function `len("apple")` runs first, and its result will be the number `5`. Then that number is compared with `3`. In other words, first the arguments of the expression are calculated (for example, the length of the string), and then the comparison operation runs.

This is how different operations are combined into more complex checks.

## Useful predicates

Strings in Python have many built-in predicate methods. They return `True` or `False` and help to check different properties of a string. The most frequently used ones are below:

```python
print("hello".startswith("he"))  # True — the string starts with "he"
print("hello".endswith("lo"))  # True — the string ends with "lo"

print("123".isdigit())  # True — all characters are digits
print("abc".isalpha())  # True — all characters are letters
print("abc123".isalnum())  # True — the string consists only of letters and digits

print("   ".isspace())  # True — the string contains only spaces
print("Hello".islower())  # False — not all characters are in lower case
print("HELLO".isupper())  # True — all characters are in upper case
print("Title Case".istitle())  # True — every word starts with a capital letter
```

Such methods let you check strings against the needed conditions right in the code, without writing additional functions.
