
Implement the function `sanitize_phone_number()`, which takes a phone number from a form and returns a string without spaces, parentheses, and hyphens.

Users type phone numbers in different ways, but applications often store them in one format. Go through the source string character by character and build a new phone number only from useful characters.

```python
sanitize_phone_number('+7 (999) 123-45-67')  # '+79991234567'
sanitize_phone_number('8 800 555 35 35')     # '88005553535'
sanitize_phone_number('(123) 456-7890')      # '1234567890'
```
