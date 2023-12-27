
Посмотрите на определение функции, которая возвращает модуль переданного числа:

```python
def abs(number):
    if number >= 0:
        return number
    return -number
```

Но можно записать более лаконично. Для этого справа от `return` должно быть выражение, но `if` — это инструкция, а не выражение. В Python есть конструкция, которая работает как `if-else`, но считается выражением. Она называется **тернарный оператор** — единственный оператор в Python, который требует три операнда:

```python
def abs(number):
    return number if number >= 0 else -number
```

Общий паттерн выглядит так: `<expression on true> if <predicate> else <expression on false>`.

Давайте перепишем начальный вариант `get_type_of_sentence()` аналогично.

Было:

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    if last_char == '?':
        return 'question'
    return 'normal'
```

Стало:

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    return 'question' if last_char == '?' else 'normal'

print(get_type_of_sentence('Hodor'))   # => normal
print(get_type_of_sentence('Hodor?'))  # => question
```

https://replit.com/@hexlet/python-basics-conditionals-ternary-operator

Тернарный оператор можно вкладывать в тернарный оператор. Но не нужно так делать, так как такой код тяжело читать и отлаживать.
