
Реализуйте функцию `is_leap_year()`, которая принимает год в форме числа и определяет является ли он високосным или нет. Год будет високосным, если он кратен (то есть делится без остатка) 400 или он одновременно кратен 4 и не кратен 100. Как видите, в определении уже заложена вся необходимая логика, осталось только переложить её на код:

```python
is_leap_year(2018) # false
is_leap_year(2017) # false
is_leap_year(2016) # true
```

Кратность можно проверять так:

```python
# % - возвращает остаток от деления левого операнда на правый
# Проверяем что number кратен 10
number % 10 == 0

# Проверяем что number не кратен 10
number % 10 != 0
```
