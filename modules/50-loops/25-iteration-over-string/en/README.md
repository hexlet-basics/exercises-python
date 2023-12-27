
Loops are used to work with strings as well as numbers. For example, you can get a specific character by its index, and also form strings in loops.

Below is some sample code that prints the letters of each word on a separate line:

```python
def print_name_by_symbol(name):
    i = 0
    # This check will run until the end of the string,
    # including the last character. Its index is `length - 1`.
    while i < len(name):
        # Accessing the symbol by its index
        print(name[i])
        i += 1

name = 'Arya'
print_name_by_symbol(name)
# => 'A'
# => 'r'
# => 'y'
# => 'a'
```

The main thing in this code is to put the proper condition in `while`. This can be done in two ways: `i < len(name)` or `i <= len(name) - 1` - they'll both give the same result.
