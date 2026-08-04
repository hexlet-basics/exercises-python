FizzBuzz es uno de los ejercicios más conocidos en las entrevistas para programadores principiantes. Se plantea para comprobar la capacidad de trabajar con bucles y condiciones. Implementa la función `fizzbuzz(n)`, que devuelve una cadena con los números del 1 al `n`.

Con estas reglas:

- si el número es divisible por 3, en su lugar se pone la palabra `"Fizz"`,
- si es divisible por 5, la palabra `"Buzz"`,
- si es divisible por 3 y por 5 a la vez, la palabra `"FizzBuzz"`.

Todos los elementos deben unirse con un espacio.

Este ejercicio aparece con frecuencia en las entrevistas para programadores, así que resulta útil saber resolverlo.

Ejemplo de llamada a la función:

```python
fizzbuzz(15)
# 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz
```

### Algoritmo

La tarea se puede resolver de distintas maneras. Un ejemplo de algoritmo:

1. Declarar el elemento neutro de la agregación (una cadena vacía)
2. Usar un bucle con los números del 1 al n
3. Comprobar las condiciones de divisibilidad del número
4. Añadir el resultado de cada iteración al resultado final separándolo con un espacio.
