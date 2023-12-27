
Реализуйте функцию-предикат `is_arguments_for_substr_correct()`, которая принимает три аргумента:

1. строку;
2. индекс, с которого начинать извлечение;
3. длину извлекаемой подстроки.

Функция возвращает `False`, если хотя бы одно из условий истинно:

* Отрицательная длина извлекаемой подстроки.
* Отрицательный заданный индекс.
* Заданный индекс выходит за границу всей строки.
* Длина подстроки в сумме с заданным индексом выходит за границу всей строки.

В ином случае функция возвращает `True`.

Не забывайте, что индексы начинаются с `0`, поэтому индекс последнего элемента — это «длина строки минус 1».

Пример вызова:

```python
string = 'Sansa Stark'
print(is_arguments_for_substr_correct(string, 2, -3))   # => False
print(is_arguments_for_substr_correct(string, -1, 3))   # => False
print(is_arguments_for_substr_correct(string, 4, 100))  # => False
print(is_arguments_for_substr_correct(string, 10, 10))  # => False
print(is_arguments_for_substr_correct(string, 11, 1))   # => False
print(is_arguments_for_substr_correct(string, 3, 3))    # => True
print(is_arguments_for_substr_correct(string, 0, 5))    # => True
```
