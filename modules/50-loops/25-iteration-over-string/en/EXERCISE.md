
Write the function `mask_card_number()`, which hides a bank card number. The function should replace every character in the string with `*`, except for the last four.

The last four characters start at index `len(card_number) - 4`. Characters with smaller indexes are replaced with `*`, and the rest stay as they are.

```python
mask_card_number("1234567812345678")  # "************5678"
mask_card_number("12345678")  # "****5678"
```
