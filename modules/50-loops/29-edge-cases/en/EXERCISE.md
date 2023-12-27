
Implement a predicate function called `is_arguments_for_substr_correct()` that takes three arguments:

1. the string
2. the index from where the extraction will begin
3. the length of the substring to be extracted

The function returns `False` if at least one of the conditions is true:

* The extracted substring has a negative length
* The index given is negative
* The index given exceeds the boundary of the entire string
* The substring length together with the given index exceeds the boundary of the whole string

Otherwise, the function returns `True`.

Don't forget that indices start with `0`, so the index of the last element is “string length minus 1”.

Call example:

```python
string = 'Sansa Stark'
print(is_arguments_for_substr_correct(string, 2, -3))   # => False
print(is_arguments_for_substr_correct(string, -1, 3))   # => False
print(is_arguments_for_substr_correct(string, 4, 100))  # => False
print(is_arguments_for_substr_correct(string, 10, 10))  # => False
print(is_arguments_for_substr_correct(string, 11, 1))   # => False
print(is_arguments_for_substr_correct(string, 3, 3))    # => True
print(is_arguments_for_substr_correct(string, 0, 5))    # => True
```
