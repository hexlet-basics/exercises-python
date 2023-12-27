
Implement a function called `normalize_url()` function, which normalizes data. It takes a site address and returns it with `https://` at the beginning.

The function accepts addresses as `ADDRESS` or `http://ADDRESS`, but always returns the address as `https://ADDRESS`. You can also pass fully normalized data, e.g., `https://ADDRESS`, in which case you don't need to change anything.

Call examples:

```python
print(normalize_url('https://yahoo.com/'))  # => 'https://yahoo.com/'
print(normalize_url('google.com'))     # => 'https://google.com'
print(normalize_url('http://ai.fi'))   # => 'https://ai.fi'
```

There are several ways to do this task. One of them is to compare the first 7 characters of the argument string with the string `http://` and then decide whether to `http://` or not based on that.

You'll also most likely need to discard the unnecessary part at the beginning of the string. Remember when we looked at the way to get part of a string using string slices? If not, here's a quick reminder

```python
# Take 6 characters from the beginning
print('Winterfell'[:6])  # => 'Winter'
```

So, with slicing, you can also discard a certain number of characters:

```python
# Discard the first 6 characters
print('Winterfell'[6:])  # => 'fell'
```
