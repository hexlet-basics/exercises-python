
Данные, вводимые пользователями, часто содержат лишние пробельные символы в конце или начале строки. Обычно их вырезают с помощью метода [.strip()](https://docs.python.org/3/library/stdtypes.html), например, было: `'   hello\n '`, стало: `'hello'`.

Обновите переменную `first_name`, записав в неё то же самое значение, но обработанное методом `.strip()`. Распечатайте то, что получилось, на экран.