
Implementa la función predicado `is_arguments_for_substr_correct()`, que toma tres argumentos:

1. Una cadena.
2. Un índice desde el cual comenzar la extracción.
3. La longitud de la subcadena a extraer.

La función devuelve `False` si al menos una de las siguientes condiciones es verdadera:

* La longitud de la subcadena a extraer es negativa.
* El índice especificado es negativo.
* El índice especificado está fuera de los límites de toda la cadena.
* La longitud de la subcadena, sumada al índice especificado, está fuera de los límites de toda la cadena.

De lo contrario, la función devuelve `True`.

No olvides que los índices comienzan en `0`, por lo que el índice del último elemento es "longitud de la cadena menos 1".

Ejemplo de llamada:

```python
string = 'Sansa Stark'
print(is_arguments_for_substr_correct(string, 2, -3))   # => False
print(is_arguments_for_substr_correct(string, -1, 3))   # => False
print(is_arguments_for_substr_correct(string, 4, 100))  # => False
print(is_arguments_for_substr_correct(string, 10, 10))  # => False
print(is_arguments_for_substr_correct(string, 11, 1))   # => False
print(is_arguments_for_substr_correct(string, 3, 3))    # => True
print(is_arguments_for_substr_correct(string, 0, 5))    # => True
```
