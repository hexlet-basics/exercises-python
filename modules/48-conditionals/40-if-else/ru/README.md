Посмотрите на функцию ниже. Она определяет тип предложения по последнему символу: если предложение заканчивается вопросительным знаком, функция вернет `Sentence is question`, иначе — `Sentence is normal`:

```python
def get_type_of_sentence(sentence: str) -> str:
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    else:
        sentence_type = 'normal'

    return "Sentence is " + sentence_type

print(get_type_of_sentence('Hodor'))  # => Sentence is normal
print(get_type_of_sentence('Hodor?')) # => Sentence is question
```

Мы добавили `else` и новый блок. Он выполнится, если условие в `if` окажется ложным. Еще в блок `else` можно вкладывать другие условия `if`. Else переводится "иначе", "в ином случае".

```text
      ┌───────────┐
      │ условие?  │
      └─────┬─────┘
  True │           │ False
      ↓           ↓
┌──────────┐ ┌──────────┐
│ тело if  │ │ тело else│
└──────────┘ └──────────┘
```

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
def get_type_of_sentence(sentence: str) -> str:
    last_char = sentence[-1]

    if last_char != '?':
        sentence_type = 'normal'
    else:
        sentence_type = 'question'

    return "Sentence is " + sentence_type
```

Чтобы конструкцию было легче оформлять, старайтесь выбирать проверку без отрицаний и подстраивайте содержимое блоков под нее.

На примере использования `else` видно, как важно не забывать отделять блоки.

```python
# Неправильно
def check_number(number):
    if number > 0:
        print("Число положительное")
    if number > 10:
        print("Число больше 10")
    else:
        print("Число не положительное")

check_number(3)
# => Число положительное
# => Число не положительное
```

В примере выше мы забыли "вложить" с помощью отступа второй `if`, поэтому `else` теперь относится ко второму `if`.

```python
# Правильно
def check_number(number: int) -> None:
    if number > 0:
        print("Число положительное")
        if number > 10:
            print("Число больше 10")
    else:
        print("Число не положительное")

check_number(3)
# => Число положительное
```

Теперь второй `if` вложен в первый, а `else` на одном уровне с первым и противопоставляется ему.
