
La función `random()` devuelve un número aleatorio entre 0 y 1 con varios decimales. Implementa un código que muestre en pantalla un número entero aleatorio en el rango de 0 a 10. Para este ejercicio, necesitarás la función `random()` y la función [round()](https://docs.python.org/3/library/functions.html#round), que redondea el valor que se le pasa.

```python
round(2.320000789855705) # 2
```

Intenta resolver este ejercicio en una sola línea.

## Algoritmo
Dado que la función `random()` devuelve números en el rango de 0 a 1, para obtener números en el rango de 0 a 10, debemos multiplicar por 10. Luego, se redondea el número resultante y así obtenemos lo que necesitamos.
