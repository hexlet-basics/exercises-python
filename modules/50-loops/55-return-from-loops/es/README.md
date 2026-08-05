El trabajo con bucles se reduce normalmente a dos escenarios. En el primero, el resultado se acumula durante las iteraciones y el trabajo con él ocurre ya después del bucle. Ese enfoque se llama agregación. Invertir una cadena pertenece a esa variante. En el segundo escenario, el bucle se ejecuta hasta alcanzar el resultado necesario y termina de forma anticipada. Así se implementa, por ejemplo, la tarea de buscar números primos, que se dividen sin resto solo entre sí mismos y entre uno.

Veamos el algoritmo de comprobación de la primalidad de un número. Dividiremos el número buscado `x` entre todos los números del rango del dos hasta `x - 1` y miraremos el resto. Si en ese rango no se encuentra un divisor que divida el número `x` sin resto, entonces ante nosotros hay un número primo.

## Comprobación de la primalidad del número 5: análisis paso a paso

1. Tomamos el número x = 5. Los divisores posibles los buscamos en el rango del 2 hasta x - 1, es decir, del 2 al 4.
2. Dividimos 5 entre 2. El resto es igual a 1, no encontramos divisor, continuamos.
3. Dividimos 5 entre 3. El resto es igual a 2, no encontramos divisor, continuamos.
4. Dividimos 5 entre 4. El resto es igual a 1, no encontramos divisor, terminamos el recorrido.

Resultado. En el rango 2…4 no se encontró ni un número entre el que 5 se divida sin resto. Por consiguiente, 5 es un número primo.

En este caso basta con limitar la búsqueda de divisores hasta la mitad del número. Por ejemplo, 11 no se divide entre 2, 3, 4, 5, y entre los números mayores que su mitad tampoco se dividirá. Eso significa que se puede optimizar el algoritmo y comprobar la división solo hasta `x / 2`:

```python
def is_prime(number: int) -> bool:
    if number < 2:
        return False

    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            return False

        divider += 1

    return True

print(is_prime(1))  # => False
print(is_prime(2))  # => True
print(is_prime(3))  # => True
print(is_prime(4))  # => False
```

*Si somos honestos hasta el final, para resolver la tarea basta con comprobar los números hasta el valor de la raíz cuadrada de `number`, pero en nuestro caso es importante centrarse en entender el trabajo con condiciones dentro de un bucle*

```text
while ...:
    if condición:
        return valor  ← salida de la función (y del bucle)
    ...
─────────────────────────
Sin return el bucle continúa hasta el final
```

Imaginemos que, según el algoritmo de división sucesiva entre los números hasta `x / 2`, se encontró uno que divide sin resto. Eso significa que el argumento recibido es un número compuesto y que los cálculos posteriores no tienen sentido. En ese punto está el retorno de `False`.

Si el bucle se ejecutó por completo y no se encontró un número que divida sin resto, entonces el número es primo.
