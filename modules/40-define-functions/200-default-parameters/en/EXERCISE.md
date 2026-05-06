
Implement a function `get_hidden_card()` that takes a credit card number (consisting of 16 digits) as a string and returns its hidden version, which can be used on the site for display. If the original card had the number *2034399002125581*, then the hidden version looks like *\*\*\*\*5581*. In other words, the function replaces the first 12 characters with asterisks. The number of asterisks is controlled by a second, optional parameter. The default value is 4.

```python
# The credit card is passed inside as a string
# The second parameter is not passed, so there will be 4 stars
get_hidden_card('1234567812345678') # ****5678

get_hidden_card('1234567812345678', 2) # **5678
get_hidden_card('1234567812345678', 3) # ***5678

# Or using variables

card_number = '2034399002121100'
get_hidden_card(card_number) # ****1100
get_hidden_card(card_number, 1) # *1100
```

To perform the task, you will need a string repetition mechanism that repeats a string a specified number of times. To do this, just multiply the string by the number of repetitions:

```python
'+' * 5 # +++++
'o' * 3 # ooo
```
