
Функция `get_type_of_sentence()` различает только вопросительные и обычные предложения. Добавим в нее поддержку восклицательных предложений:

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'

    if last_char == '!':
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'

    return 'Sentence is ' + sentence_type

print(get_type_of_sentence('Who?'))  # => 'Sentence is normal'
print(get_type_of_sentence('No'))    # => 'Sentence is normal'
print(get_type_of_sentence('No!'))   # => 'Sentence is exclamation'
```

https://replit.com/@hexlet/python-basics-conditionals-elif

Мы добавили проверку восклицательных предложений — exclamation. Технически эта функция работает, но вопросительные предложения трактует неверно. Еще в ней есть проблемы с точки зрения семантики:

* Наличие восклицательного знака проверяется в любом случае, даже если уже обнаружился вопросительный знак
* Ветка `else` описана для второго условия, но не для первого. Поэтому вопросительное предложение становится `"normal"`

Чтобы исправить ситуацию, воспользуемся еще одной возможностью условной конструкции:

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    elif last_char == '!':
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'

    return 'Sentence is ' + sentence_type

print(get_type_of_sentence('Who?'))  # => 'Sentence is question'
print(get_type_of_sentence('No'))    # => 'Sentence is normal'
print(get_type_of_sentence('No!'))   # => 'Sentence is exclamation'
```

Теперь все условия выстроились в единую конструкцию. `elif` означает — «если не выполнено предыдущее условие, но выполнено текущее». Получается такая схема:

* если последняя буква `?`, то `'question'`
* если последняя буква `!`, то `'exclamation'`
* остальные варианты — `'normal'`

Выполнится только один из блоков кода, который относится ко всей конструкции `if`.
