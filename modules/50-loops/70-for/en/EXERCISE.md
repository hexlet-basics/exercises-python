
In a previous lesson, we already wrote the `filter_string()` function. Recall that it takes a string and a character as input and returns a new string in which the passed character at all its positions is removed. This time, implement this function using the `for` loop. An additional condition: the case of the character to be eliminated does not matter.

An example of a call:

```python
text = 'If I look forward I win'
filter_string(text, 'i')  # 'f  look forward  wn'
filter_string(text, 'O')  # 'If I lk frward I win'
```
