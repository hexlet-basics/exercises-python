На электронной карте Вестероса, которую реализовал Сэм, союзники Старков отображены зеленым кружком, враги — красным, а нейтральные семьи — серым.

Напишите для Сэма функцию `who_is_this_house_to_starks()`, которая принимает на вход фамилию семьи и возвращает одно из трех значений: `'friend'`, `'enemy'`, `'neutral'`.

Правила определения:

  * Друзья (`'friend'`): `'Karstark'`, `'Tully'`
  * Враги (`'enemy'`): `'Lannister'`, `'Frey'`
  * Любые другие семьи считаются нейтральными (`'neutral'`)

Примеры вызова:

```python
print(who_is_this_house_to_starks('Karstark'))  # => 'friend'
print(who_is_this_house_to_starks('Frey'))      # => 'enemy'
print(who_is_this_house_to_starks('Joar'))      # => 'neutral'
print(who_is_this_house_to_starks('Ivanov'))    # => 'neutral'
```
