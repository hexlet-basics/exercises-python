
Implement a function called `my_substr()` that extracts a substring of a specified length from a string. It takes two arguments as input: a string and a length, and returns a substring starting from the first character:

Call example:

```python
string = 'If I look back I am lost'
print(my_substr(string, 1)) # => 'I'
print(my_substr(string, 7)) # => 'If I lo'
```

Use the same approach as in the function to flip the string from the lesson: assemble the resulting string with a loop by looping over the initial string to a certain point.

This problem can be solved using slicing. But in this exercise, we want to practice using loops, so we'll implement this functionality ourselves. Slice syntax essentially uses loops anyway.
