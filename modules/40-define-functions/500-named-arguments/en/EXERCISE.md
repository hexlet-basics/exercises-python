
Implement a function `trim_and_repeat()` that takes three parameters: the string, `offset` - the number of characters by which to trim the string to the left and `repetitions` - the number of times it needs to be repeated, and returns the resulting string.
The default number of characters to cut is 0, and the number of repetitions is 1.

```python
text = 'python'
print(trim_and_repeat(text, offset=3, repetitions=2)) # => honhon
print(trim_and_repeat(text, repetitions=3)) # => pythonpythonpython
print(trim_and_repeat(text)) # => python
```
