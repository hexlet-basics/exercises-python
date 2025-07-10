
Агрегация строк — это такие задачи, в которых заранее неизвестно, что содержат строки и какой у них размер.

Представьте функцию, которая умеет умножать строку — повторяет ее указанное количество раз:

```python
repeat('hexlet', 3)  # 'hexlethexlethexlet'
```

Принцип работы этой функции — в цикле происходит «наращивание» строки указанное количество раз:

```python
def repeat(text, times):
    # Нейтральный элемент для строк — пустая строка
    result = ''
    i = 1

    while i <= times:
        # Каждый раз добавляем строку к результату
        result = result + text
        i = i + 1

    return result
```


Распишем выполнение этого кода по шагам:

```python
# Для вызова repeat('hexlet', 3)
result = ''
result = result + 'hexlet'  # hexlet
result = result + 'hexlet'  # hexlethexlet
result = result + 'hexlet'  # hexlethexlethexlet
```
