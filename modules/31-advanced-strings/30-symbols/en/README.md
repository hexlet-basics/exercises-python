
Sometimes, you have to get a single character from a string. For example, if a site knows users' first and last names, and at some point you want it to output this information in a format like *J. Smith*. To do this, the computer will need to take the first character from the name. Python has a suitable operation, which is what we'll study today.

Suppose you want to display only the first letter of the name Alexander. It looks like this:

```python
first_name = 'Alexander'

print(first_name[0])  # => A
```

The operation with square brackets with a digit extracts an element by **index** - the position of the character inside the string. Indexes start with 0 in almost all programming languages. Therefore, to get the first character, you must specify the index `0`. The index of the last element is equal to the string length minus one. Accessing an index outside the string will cause an error:

```python
# The string length is 9, so the last index is 8
first_name = 'Alexander'

print(first_name[8])  # => r

print(first_name[9])
IndexError: string index out of range
```

To better consolidate your new knowledge, look at the code below and think about what it produces:

```python
magic = '\nyou'
print(magic[1])  # => ?
```

There are, of course, non-standard situations. For example, you need to output an element from the end, and it's from an expression with a large number of characters. In this case, you can use the negative index, which will make your life much easier.

You're allowed to use negative indices. In this case, we access characters starting from the end of the string. `-1` is the index of the last character, `-2` is the penultimate, and so on. Unlike direct indexing, the countdown is from `-1`:

```python
first_name = 'Alexander'

print(first_name[-1])  # => r
```

You can use variables as well as numbers as an index. Look at the example below. Here we have an index inside the square brackets, but it's not a number, it's a variable. This code will cause the same result it'll output  *A*:

```python
first_name = 'Alexander'
index = 0

print(first_name[index])  # => A
```

If you only want to get a few characters from an expression, you don't need to write a large number of lines of code, just extract the element using an index. You can also use a negative index to make it easier to output characters from the end of an expression. Next, let's see how this knowledge can be used to extract a substring from a string.
