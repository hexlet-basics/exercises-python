Las **operaciones lógicas** son expresiones, por eso se pueden combinar con otras expresiones. Por ejemplo, queremos comprobar la paridad de un número, es decir, si es múltiplo de dos. En programación, para eso se comprueba el resto de la división entre dos. Si el resto es igual a `0`, el número es par. Si el resto no es igual a `0`, el número es impar.

El resto de la división es un concepto simple pero importante en aritmética, álgebra, teoría de números y criptografía. Hay que dividir un número en varios grupos iguales, y si al final queda algo, eso es precisamente el resto de la división.

Repartimos caramelos a partes iguales entre personas:

- 7 caramelos, 2 personas: 2 x 3 + resto 1 (7 no es múltiplo de 2)
- 21 caramelos, 3 personas: 3 x 7 + resto 0 (21 es múltiplo de 3)
- 19 caramelos, 5 personas: 5 x 3 + resto 4 (19 no es múltiplo de 5)

El operador `%` calcula el resto de la división:

- `7 % 2` → `1`
- `21 % 3` → `0`
- `19 % 5` → `4`

Combinemos en una misma expresión el operador lógico de "comprobación de igualdad" `==` y el operador aritmético `%`, y escribamos una función de comprobación de la paridad:

```python
def is_even(number: int) -> bool:
    return number % 2 == 0


print(is_even(10))  # => True
print(is_even(3))  # => False
```

La prioridad de las operaciones aritméticas es mayor que la de las lógicas. Eso significa que primero se evalúa la expresión aritmética `number % 2` y luego el resultado se compara con cero y se devuelve el resultado de la comprobación de igualdad.

Ahora escribamos una función que recibe una cadena y comprueba si esa cadena empieza por la letra latina `a`.

El algoritmo:

1. Obtenemos y guardamos en una variable el primer carácter de la cadena-argumento
2. Comparamos si el carácter es igual a la letra latina `a`
3. Devolvemos el resultado

```python
def is_first_letter_an_a(text: str) -> bool:
    first_letter = text[0]
    return first_letter == "a"


print(is_first_letter_an_a("orange"))  # => False
print(is_first_letter_an_a("apple"))  # => True
```

Para que quede claro qué ocurre aquí, intenta decir en voz alta lo que pasa, igual que descifrábamos el proceso en el ejemplo con `is_even()`.

Ahora sabes que las operaciones de comparación se aplican en programación al mismo nivel que las aritméticas. Pero recuerda que la igualdad se denota con `==`. Así no confundirás esa operación con la asignación de un valor a una variable.
