Рассмотрим пример программы, которая выполняет конвертацию валют:

```python
euros_count = 1000
dollars_count = euros_count * 1.25  # 1250.0
rubles_count = dollars_count * 60   # 75000.0

print(rubles_count)
```

С технической точки зрения — всё работает. Но с точки зрения профессиональной разработки такой код считается плохой практикой.

## 🤨 В чём проблема?

В выражениях использованы непонятные числа: __1.25__ и __60__. Что это за значения? Курс валют? Откуда они взялись? Через месяц или год вы, скорее всего, не вспомните, что именно означают эти числа. А если код откроет другой разработчик, он просто не поймёт, откуда всё берётся.

## 🔍 Такие значения называют «магическими числами»

Магические числа (magic numbers) — это числовые значения, смысл которых не ясен из кода. Чтобы понять их назначение, приходится вникать в контекст или читать дополнительную документацию. Магические числа затрудняют чтение, понимание и поддержку кода.

## ✅ Как избежать магии

Самый простой способ — вынести такие значения в переменные с понятными именами. Тогда смысл станет очевиден:

```python
dollars_per_euro = 1.25
rubles_per_dollar = 60

euros_count = 1000
dollars_count = euros_count * dollars_per_euro      # 1250.0
rubles_count = dollars_count * rubles_per_dollar    # 75000.0

print(rubles_count)
```

## 📌 Что изменилось?

- Значения вынесены в отдельные переменные с осмысленными именами.
- Используется snake_case — стандарт стиля в Python.
- Отделили данные от логики: сначала определили курсы, потом сделали вычисления.
- Добавили пустую строку между «исходными данными» и вычислениями — это повышает читаемость.
- Программа стала немного длиннее, но понятнее. И это — норма.

💬 Вывод

Магические числа делают код непонятным и трудным для поддержки. Чтобы избежать этой проблемы, нужно заменять такие числа переменными с осмысленными именами. Это делает код более читаемым, особенно в долгосрочной перспективе. Не стоит бояться того, что программа станет чуть длиннее — понятный код всегда важнее компактности.
