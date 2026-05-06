Реализуйте функцию `has_at_symbol()`, которая проверяет, есть ли в email символ `@`.

Функция должна вернуть `True`, как только найдет `@`. Если цикл дошел до конца строки и символ не найден, функция должна вернуть `False`.

```python
has_at_symbol('support@example.com')  # True
has_at_symbol('wrong-email')          # False
has_at_symbol('@admin')               # True
```
