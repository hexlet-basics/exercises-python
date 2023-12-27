
The electronic map of Westeros that Sam implemented shows Stark allies in green circles, enemies in red, and neutral families in gray.

Write a function `who_is_this_house_to_starks()` for Sam that takes the family name as input and returns one of three values: `'friend'`, `'enemy'`, `'neutral'`.

Rules of Determination:

  * Friends (`'friend'`): `'Karstark'`, `'Tully'`
  * Enemies (`'enemy'`): `'Lannister'`, `'Frey'`
  * Any other families are considered `neutral'`.

Examples of calls:

```python
print(who_is_this_house_to_starks('Karstark'))  # => 'friend'
print(who_is_this_house_to_starks('Frey'))      # => 'enemy'
print(who_is_this_house_to_starks('Joar'))      # => 'neutral'
print(who_is_this_house_to_starks('Ivanov'))    # => 'neutral'
```
