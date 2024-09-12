
Многие языки в дополнение к условной конструкции `if` включают в себя `switch`. С выходом версии Python 3.10 также был добавлен оператор с аналогичной функциональностью — `match`. В этом уроке мы познакомимся с этим оператором.

Оператор `match` — это специализированная версия `if`, которую создали для особых ситуаций. Например, ее нужно использовать там, где есть цепочка `if else` с проверками на равенство:

```python
if status == 'processing':
    # Делаем раз
elif status == 'paid':
    # Делаем два
elif status == 'new':
    # Делаем три
else:
    # Делаем четыре
```

У этой составной проверки есть одна отличительная черта: каждая ветка здесь — это проверка значения переменной `status`. Оператор `match` позволяет записать этот код короче и выразительнее:

```python
match status:
    case 'processing':  # status == 'processing'
        # Делаем раз
    case 'paid':  # status == 'paid'
        # Делаем два
    case 'new':  # status == 'new'
        # Делаем три
    case _:  # else
        # Делаем четыре
```

С точки зрения количества элементов `match` — это сложная конструкция. Она состоит из таких элементов:

* Внешнее описание, в которое входит ключевое слово `match`. Это переменная, по значениям которой `match` будет выбирать поведение
* Конструкции `case`, внутри которой описывается поведение для разных значений рассматриваемой переменной. Каждый `case` соответствует `if` в примере выше. При этом `case _` — это особая ситуация, которая соответствует ветке `else` в условных конструкциях. Как и `else`, указывать `case _` необязательно

Внутри `match` допустим только тот синтаксис, который показан выше. Другими словами, там можно использовать `case`. А вот внутри каждого `case` ситуация другая. Здесь можно выполнять любой произвольный код:

```python
match count:
    case 1:
        # Делаем что-то полезное
    case 2:
        # Делаем что-то полезное
    case _:
        # Что-то делаем
```

Иногда результат, полученный внутри `case` — это конец выполнения функции, которая содержит `match`. В таком случае его нужно как-то вернуть наружу. Для решения этой задачи есть два способа:

Первый. Создать переменную перед `match`, заполнить ее в `case` и затем в конце вернуть значение этой переменной наружу:

```python
def count_items(count):
    # Объявляем переменную
    result = ''

    # Заполняем
    match count:
        case 1:
            result = 'one'
        case 2:
            result = 'two'
        case _:
            result = None

    # Возвращаем
    return result
```

Второй способ проще и короче. Вместо создания переменной при работе с `case` можно делать обычный возврат из функции:

```python
def count_items(count):
    match count:
        case 1:
            return 'one'
        case 2:
            return 'two'
        case _:
            return None
```

Оператор `match` хоть и встречается в коде, но технически всегда можно обойтись без него. Ключевая польза при его использовании в том, что он лучше выражает намерение программиста, когда нужно проверять конкретные значения переменной. Хотя кода и стало физически чуть больше, читать его легче, в отличие от блоков `elif`.