
Like with number aggregation, string aggregation involves not knowing what the strings contain and how big they are.

Imagine a function that knows how to multiply a string; it repeats it a specified number of times:

```python
repeat('hexlet', 3)  # 'hexlethexlethexlet'
```

The principle of how this function works is that in the loop, the string is “incremented” a specified number of times:

```python
def repeat(text, times):
    # The neutral element for strings is an empty string
    result = ''
    i = 1

    while i <= times:
        # Each time we add the string to the result
        result = result + text
        i = i + 1

    return result
```

Let's break down the code's execution into steps:

```python
# To call repeat('hexlet', 3)
result = ''
result = result + 'hexlet'  # hexlet
result = result + 'hexlet'  # hexlethexlet
result = result + 'hexlet'  # hexlethexlethexlet
```
