Un formulario del sitio recibe datos del usuario. Antes de procesar el valor, el programa comprueba que en el campo del nombre se pasó una cadena y no un número u otro tipo. Implementa la función `string_or_not()`, que comprueba si el parámetro recibido es una cadena. Si lo es, devuelve `'yes'`; en caso contrario, `'no'`

```python
string_or_not('Hexlet') # 'yes'
string_or_not(10) # 'no'
string_or_not('') # 'yes'
string_or_not(False) # 'no'
```

Comprobar si el parámetro recibido es una cadena se puede hacer con la función [isinstance()](https://docs.python.org/3/library/functions.html#isinstance):

```python
isinstance(3, str) # False
isinstance('Hexlet', str) # True
```
