
Implementa la función `string_or_not()` que verifica si el parámetro proporcionado es una cadena correcta. Si lo es, devolverá como resultado `'yes'`, de lo contrario, devuelve `'no'`

```python
string_or_not('Hexlet') # 'yes'
string_or_not(10) # 'no'
string_or_not('') # 'yes'
string_or_not(False) # 'no'
```

Puedes verificar si el parámetro proporcionado es una cadena utilizando la función [isinstance()](https://docs.python.org/3/library/functions.html#isinstance):

```python
isinstance(3, str) # False
isinstance('Hexlet', str) # True
```
