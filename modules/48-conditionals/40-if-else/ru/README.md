
Теперь изменим функцию из предыдущего урока так, чтобы она возвращала не просто тип предложения, а целую строку `Sentence is normal` или `Sentence is question`:

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    else:
        sentence_type = 'normal'

    return "Sentence is " + sentence_type

print(get_type_of_sentence('Hodor'))   # => 'Sentence is normal'
print(get_type_of_sentence('Hodor?'))  # => 'Sentence is question'
```

https://replit.com/@hexlet/python-basics-conditionals-if-else

Мы добавили `else` и новый блок. Он выполнится, если условие в `if` — ложь. Еще в блок `else` можно вкладывать другие условия `if`. Else переводится «иначе», «в ином случае».

Пример вложенных блоков:

```python
number = 10

if number > 10:
    print("Number is greater than 10")
else:
    if number == 10:
        print("Number is exactly 10")
    else:
        print("Number is less than 10")
```

Оформить конструкцию `if-else` можно двумя способами. С помощью отрицания можно изменить порядок блоков:

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char != '?':
        sentence_type = 'normal'
    else:
        sentence_type = 'question'

    return "Sentence is " + sentence_type
```

Чтобы конструкцию было легче оформлять, старайтесь выбирать проверку без отрицаний и подстраивайте содержимое блоков под нее.
