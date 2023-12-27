
Реализуйте функцию `trim_and_repeat()`, которая принимает три параметра: строку, `offset` — число символов, на которое нужно обрезать строку слева и `repetitions` — количество обрезанных строк, которые нужно вывести. Функция обрезает строку и повторяет ее столько раз, чтобы общее количество обрезанных строк равнялось `repetitions`. Функция должна записать результат в одну строку и вернуть его.
Число символов для среза по умолчанию равно 0, а повторений — 1.

```python
text = 'python'
print(trim_and_repeat(text, offset=3, repetitions=2)) # => honhon
print(trim_and_repeat(text, repetitions=3)) # => pythonpythonpython
print(trim_and_repeat(text)) # => python
```
