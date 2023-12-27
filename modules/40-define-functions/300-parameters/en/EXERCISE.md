
Create a function called `truncate()` that truncates a string passed to it to a specified number of characters, adds an ellipsis at the end, and returns the resulting string. This kind of logic is often used on websites to display long text in shortened form.

The function takes two parameters:

1. The string to be trimmed
2. Number of characters to leave

An example of how the function you wrote should work:

```python
# Pass text directly
# Truncate the text, leaving two characters
truncate('hexlet', 2)  # 'he...'

# Via a variable
text = 'it works!'
# Truncate the text, leaving 4 characters
truncate(text, 4)  # 'it w...'
```

There are lots of ways you can do this task, we'll tell you just one of them. To solve it this way, you need to take a substring from the string passed as the first parameter to the function. Use string slices to do this. Think, based on the assignment, from which index and by which one do you need to extract the substring?

```python
word = 'welcome!'
index = 3
word[:index] # wel
```
