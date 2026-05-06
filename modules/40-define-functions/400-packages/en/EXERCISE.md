Implement the function `generate_pin()`. It returns a random four-digit PIN code as a string.

Each digit of the PIN is an independent random integer from 0 to 9.

```python
print(generate_pin())  # => e.g. "4823" or "0571"
print(generate_pin())  # => e.g. "1942" or "0037"
```

Add a return type annotation.

## Hint

Generate each of the four digits with `random.randint(0, 9)` and combine them into a string using an f-string.
