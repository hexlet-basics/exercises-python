Finish the function `truncate()`, which cuts the given string down to the specified number of characters, adds an ellipsis at the end and returns the resulting string. Logic like this is often used on sites to show long text in a shortened form.

The function takes two parameters:

1. The string that has to be cut
2. The number of characters to keep

An example of how the function you write should behave:

```python
# Passing the text directly
# Cutting the text down to 2 characters
truncate('hexlet', 2)  # 'he...'

# Through a variable
text = 'it works!'
# Cutting the text down to 4 characters
truncate(text, 4)  # 'it w...'
```

The task can be solved in several ways; we will hint at just one of them. For that way you need to take a substring of the string passed as the first parameter. Use string slices for this. Based on the task, think about which index you have to extract the substring from and to:

```python
word = 'welcome!'
index = 3
word[:index] # wel
```
