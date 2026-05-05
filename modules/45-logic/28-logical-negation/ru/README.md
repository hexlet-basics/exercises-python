Наряду с логическими операторами **И** и **ИЛИ**, часто используется операция "**отрицание**". Она меняет логическое значение на противоположное. В Python отрицанию соответствует унарный оператор `not` (в других языках `!`):

```python
not True   # False
not False  # True
```

Например, если есть функция, которая проверяет четность числа, то с помощью отрицания можно выполнить проверку нечетности:

```python
def is_even(number: int) -> bool:
    return number % 2 == 0

print(is_even(10))      # => True
print(not is_even(10))  # => False
```

В примере выше мы добавили `not` слева от вызова функции и получили обратное действие.

Отрицание позволяет выражать задуманные правила в коде без написания новых функций. Если написать `not not is_even(10)`, то код сработает даже в таком случае:

```python
print(not not is_even(10))  # => True
```

В логике двойное отрицание равносильно отсутствию отрицания:

```python
not not True   # True
not not False  # False

print(not not is_even(10))  # => True
print(not not is_even(11))  # => False
```

`not` можно комбинировать с `and` и `or`. Среди логических операторов у него наивысший приоритет, поэтому он применяется первым:

```python
not True or True    # (not True) or True   => False or True  => True
not True and False  # (not True) and False => False and False => False
```

Скобки меняют порядок вычисления:

```python
not (True or True)   # not True  => False
not (True and False) # not False => True
```

Практический пример — функция проверяет, может ли водитель сесть за руль: нужны права и трезвость:

```python
def can_drive(has_license: bool, is_drunk: bool) -> bool:
    return has_license and not is_drunk

print(can_drive(True, False))   # => True  (есть права, трезвый)
print(can_drive(True, True))    # => False (есть права, но пьяный)
print(can_drive(False, False))  # => False (нет прав)
```

Теперь вы знаете, что означают операторы **И**, **ИЛИ** и `not`. С их помощью вы сможете задавать составные условия из двух и более логических выражений.

## Законы де Моргана

При работе со сложными логическими выражениями бывает нужно их инвертировать или переписать в эквивалентную форму, которую легче читать. Для этого существуют **законы де Моргана** - два правила, которые описывают, как отрицание распределяется по составному выражению:

```python
not (A and B)  ==  not A or not B
not (A or B)   ==  not A and not B
```

Первый закон: отрицание конъюнкции равно дизъюнкции отрицаний. Проверим:

```python
not (True and False)      # not False => True
not True or not False     # False or True => True
```

Второй закон: отрицание дизъюнкции равно конъюнкции отрицаний:

```python
not (True or False)       # not True => False
not True and not False    # False and True => False
```

На практике законы де Моргана помогают упрощать условия. Например, вместо `not (is_admin or is_moderator)` можно написать `not is_admin and not is_moderator` — читается как "не администратор и не модератор".
