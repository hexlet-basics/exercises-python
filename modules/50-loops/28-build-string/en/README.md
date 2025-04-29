
You can also use loops to form strings. This is often needed during web programming. It all comes down to the usual aggregation when interpolation or concatenation is applied.

You'll often be asked to write a program to reverse a string in interviews. The correct way to flip a string is to use a function from the standard library. But it's important to know how to actually implement it yourself.

One of the algorithms looks like this:

1. Build a new string

2. Go through the characters of the original string in reverse order

```python
def reverse_string(string):
    index = len(string) - 1
    reversed_string = ''

    while index >= 0:
        current_char = string[index]
        reversed_string = reversed_string + current_char
        # The same through interpolation
        # reversed_string = f'{reversed_string}{current_char}'
        index = index - 1

    return reversed_string

reverse_string('Game Of Thrones')  # 'senorhT fO emaG'
# Neutral element check
reverse_string('')  # ''
```

Let's analyze the function line by line:

* `index = len(string) - 1` - we write the index of the last character of the string into a new variable (remember indexes start with zero)
* `reversed_string = ''` - initialize the string that we'll write the result to
* `while index >= 0:` - condition: repeat the body of the loop until the current index reaches `0` - (the first character)
* `current_char = string[index]` - take the character at the current index from the string
* `reversed_string = reversed_string + current_char` - write the new value to the string with the result: current string is the result + the new character
* `index = index - 1` - update the counter
* `return reversed_string` - when the loop is done, return the result string

When working with strings, programmers often make the mistake of going past string boundaries. If a wrong initial counter value is chosen or a mistake is made in a loop predicate, the function may access a character that doesn't exist.

It's also extremely often forgotten that the index of the last element is always one less than the size of the string. In strings, the initial index is `0`, so the index of the last element is `len(str) - 1`.
