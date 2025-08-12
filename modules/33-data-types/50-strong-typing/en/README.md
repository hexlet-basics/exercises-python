
Python is one of the languages that is strict about data types. So it will respond to any type incompatibility with an error. It is all about strong typing.

We know about two different types of data: numbers and strings. For example, we could add numbers, because the addition operation is an operation for the "numbers" type. But what if we applied this operation not to two numbers, but to a number and a string?

```python
print(1 + '7')  # TypeError: unsupported operand type(s)...
```

Python will not allow adding the number `1` and the string `'7'`, because they are of different types. You have to first either make the string a number or the number a string. We'll talk about how to do that later.

This pedantic attitude towards type compatibility is called **strict typing** or **strong typing**. Python is a language with strict typing.

Not all languages do this. For example, PHP is a language with **weak typing**. It is aware of the existence of different types, but is not very strict about their use. PHP tries to convert information when it makes sense. The same goes for JavaScript:

```php
// What do you think of that, Elon Musk?
// Number 1 + Line 7 = Line 17
1 + '7'; // '17'
```

On the one hand, automatic implicit type conversion does seem convenient. But in practice this language's property creates a lot of errors and problems that are hard to find. The code may sometimes work and sometimes not work, depending on whether you have "luck" with automatic conversion or not. The programmer will not notice this immediately and will spend a lot of time on debugging.
