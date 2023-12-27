
Implementa el método `is_leap_year()`, que determina si un año es bisiesto o no. Un año es bisiesto si es divisible (es decir, no tiene residuo) por 400 o si es divisible por 4 y no es divisible por 100 al mismo tiempo. Como puedes ver, toda la lógica necesaria ya está incluida en la definición, solamente falta trasladarla al código:

```python
is_leap_year(2018) # false
is_leap_year(2017) # false
is_leap_year(2016) # true
```

Puedes verificar la divisibilidad de la siguiente manera:

```python
# % - devuelve el residuo de la división del operando izquierdo por el operando derecho
# Verifica si number es divisible por 10
number % 10 == 0

# Verifica si number no es divisible por 10
number % 10 != 0
```
