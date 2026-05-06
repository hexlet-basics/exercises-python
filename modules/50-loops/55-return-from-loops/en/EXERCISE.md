
Implement the function `has_at_symbol()`, which checks whether an email contains the `@` symbol.

The function should return `True` as soon as it finds `@`. If the loop reaches the end of the string and the symbol is not found, the function should return `False`.

```python
has_at_symbol('support@example.com')  # True
has_at_symbol('wrong-email')          # False
has_at_symbol('@admin')               # True
```
