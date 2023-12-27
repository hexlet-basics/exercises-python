
Trabajar con bucles generalmente se reduce a dos escenarios:

1. Agregación. Acumular resultados durante las iteraciones y trabajar con ellos después del bucle. Voltear una cadena es un ejemplo de este caso.
2. Ejecutar el bucle hasta que se alcance un resultado deseado y luego salir. Por ejemplo, la tarea de encontrar números primos, que solo son divisibles exactamente por sí mismos y por uno.

Veamos el algoritmo para comprobar si un número es primo. Dividiremos el número buscado `x` entre todos los números en el rango desde dos hasta `x - 1` y observaremos el residuo. Si no encontramos ningún divisor en este rango que divida al número `x` sin residuo, entonces estamos ante un número primo.

En este caso, solo es necesario verificar los números hasta `x / 2`, en lugar de hasta `x - 1`. Por ejemplo, 11 no es divisible por 2, 3, 4, 5. Pero tampoco será divisible por números mayores que la mitad de sí mismo. Por lo tanto, podemos optimizar el algoritmo y verificar la división solo hasta `x / 2`:

```python
def is_prime(number):
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

https://replit.com/@hexlet/python-basics-loops-return-from-loops

*Siendo completamente honestos, para resolver el problema es suficiente verificar los números hasta la raíz cuadrada de `numero`, pero en nuestro caso es importante concentrarse en comprender las condiciones dentro del bucle.*

Imaginemos que en el algoritmo de división secuencial de números hasta `x / 2` encontramos uno que divide sin residuo. Entonces, el argumento proporcionado no es un número primo y no tiene sentido continuar con los cálculos. En este punto, deberíamos retornar `False`.

Si el bucle se ejecuta por completo y no encontramos ningún número que divida sin residuo, entonces el número es primo.
