Las operaciones de comparación funcionan con números y con cadenas. En Python las cadenas se comparan lexicográficamente: carácter por carácter, de izquierda a derecha, por los códigos numéricos de los caracteres (Unicode).

```python
print("apple" < "banana")   # => True
print("cat" > "dog")        # => False
print("abc" == "abc")       # => True
print("hello" != "world")   # => True
```

Aquí `"apple" < "banana"` porque el código de `a` (97) es menor que el código de `b` (98), y es precisamente el primer carácter el que decide el resultado de la comparación. El código de un carácter se puede ver así: `ord('a')` → `97`.

```python
print(ord("a")) # => 97
print(ord("b")) # => 98
```

La comparación distingue mayúsculas y minúsculas: `'Z'` (90) < `'a'` (97). Un ejemplo de comparación en el que las primeras letras son de distinto caso:

```python
print("Zebra" < "apple")    # True — 'Z'(90) < 'a'(97)
print("apple" < "Banana")   # False — 'a'(97) > 'B'(66)
print("Apple" < "apple") # True  —  'A'(65) < 'a'(97)
```

Escribamos una función que comprueba si una palabra empieza por una letra dada. Para eso tomamos el primer carácter de la cadena y lo comparamos con la letra necesaria.

```python
def starts_with(word: str, letter: str) -> bool:
    return word[0] == letter

print(starts_with("apple", "a"))   # => True
print(starts_with("banana", "a"))  # => False
```

Las operaciones de comparación son expresiones igual que las aritméticas. En ellas se pueden sustituir valores ya listos y otras expresiones, como en el ejemplo de arriba: `word[0]`. Por ejemplo, en lugar de un número se puede usar el resultado del trabajo de la función `len`, que devuelve la longitud de una cadena:

```python
print(len("apple") > 3)   # => True, porque len("apple") = 5
print(len("hi") > 3)      # => False, porque len("hi") = 2
```

En el ejemplo de arriba se ejecuta primero la función `len("apple")`, cuyo resultado será el número `5`. Después ese número se compara con `3`. En otras palabras, primero se calculan los argumentos de la expresión (por ejemplo, la longitud de la cadena) y luego se ejecuta la operación de comparación.

Así se pueden combinar distintas operaciones, obteniendo comprobaciones más complejas.

## Predicados útiles

Las cadenas en Python tienen muchos métodos-predicado incorporados. Devuelven `True` o `False` y ayudan a comprobar distintas propiedades de la cadena. Abajo están los que se usan con más frecuencia:

```python
print("hello".startswith("he"))   # True — la cadena empieza por "he"
print("hello".endswith("lo"))     # True — la cadena termina en "lo"

print("123".isdigit())            # True — todos los caracteres son dígitos
print("abc".isalpha())            # True — todos los caracteres son letras
print("abc123".isalnum())         # True — la cadena consta solo de letras y dígitos

print("   ".isspace())            # True — la cadena contiene solo espacios
print("Hello".islower())          # False — no todos los caracteres están en minúscula
print("HELLO".isupper())          # True — todos los caracteres están en mayúscula
print("Title Case".istitle())     # True — cada palabra empieza por mayúscula
```

Esos métodos permiten comprobar las cadenas según las condiciones necesarias directamente en el código, sin escribir funciones adicionales.
