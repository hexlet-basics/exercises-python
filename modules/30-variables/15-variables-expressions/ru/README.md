Мы уже знаем, что переменные позволяют хранить и переиспользовать данные. Но они также помогают упрощать вычисления — как математические, так и строковые. Рассмотрим это на примерах.

## 💱 Конвертация валют через промежуточную валюту

Представим, что нужно перевести евро в юани, но напрямую такой курс нам недоступен. Тогда сделаем это в два шага: **евро → доллары → юани**. Так часто работают банки при оплате покупок за рубежом.

## Шаг 1. Евро → Доллары

Допустим, курс: 1 евро = 1.25 доллара. Хотим перевести 50 евро:

```python
dollars_count = 50 * 1.25
print(dollars_count)  # => 62.5
```

В этой строке 50 \* 1.25 — это выражение, а dollars_count — переменная, в которую записывается результат. Python сначала вычисляет выражение, а уже потом сохраняет результат в переменную.

Интерпретатору всё равно, как записано выражение:

```python
dollars_count = 62.5
```

или

```python
dollars_count = 50 * 1.25
```

Результат будет один и тот же.

## 📘 Что такое выражение?

Выражение — это комбинация данных и операций, из которой можно получить значение.
Примеры:

```python
62.5             # 62.5
50 * 1.25        # 62.5
120 / 10 * 2     # 24.0
int('100')       # 100

'hello'          # hello
'Good' + 'will'  # Goodwill
```

Обратите внимание: строки — это тоже выражения. А операция + со строками называется конкатенацией — она "склеивает" строки в одну.

Если вы понимаете, что перед вами выражение, вы знаете: Python сначала его вычислит, а уже потом продолжит выполнение программы. Это особенно важно, когда выражения становятся сложными и включают переменные, функции и даже другие выражения внутри.

## ✨ Пример со строками

Подумайте, сработает ли такой код:

```python
who = "dragon's " + 'mother'
print(who)
```

Ответ: да, всё отлично сработает. На экран выведется строка: _dragon's mother_

## Шаг 2. Доллары → Юани

Теперь переведем 50 евро в юани, используя доллар, как промежуточную валюту. Допустим, курсы валют: 1 доллар = 6.91 юаней, 1 евро = 1.25 долларов.

```python
yuans_per_dollar = 6.91
dollars_count = 50 * 1.25              # 62.5
yuans_count = dollars_count * yuans_per_dollar  # 431.875

print(yuans_count)
```

Переменные можно использовать внутри других выражений. Когда Python видит переменную, он подставляет её значение, а затем выполняет вычисления.

## 📌 Что нужно запомнить

- Выражения могут быть числовыми, строковыми и даже смешанными (если правильно использовать преобразования).
- Переменные можно использовать внутри других выражений. Python подставит их значения и выполнит нужные вычисления.
- Все программы состоят из комбинаций выражений — именно они дают результат.
