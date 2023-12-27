
Implement a function `string_or_not()` that checks if the passed parameter is a string. If yes, it returns `'yes'` otherwise `'no'`.

```python
string_or_not('Hexlet') # 'yes'
string_or_not(10) # 'no'
string_or_not('') # 'yes'
string_or_not(False) # 'no'
```

You can check if the passed parameter is a string with the function [isinstance()](https://docs.python.org/3/library/functions.html#isinstance):

```python
isinstance(3, str) # False
isinstance('Hexlet', str) # True
```

Experiment with the code in the interactive replay https://replit.com/@hexlet/python-basics-logical-expressions
