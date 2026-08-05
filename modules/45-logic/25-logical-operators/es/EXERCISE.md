Implementa la función `is_leap_year()`, que recibe un año en forma de número y determina si es bisiesto o no. Un año será bisiesto si es múltiplo de (es decir, se divide sin resto entre) 400, o si a la vez es múltiplo de 4 y no es múltiplo de 100. Como ves, en la definición ya está contenida toda la lógica necesaria; solo queda trasladarla al código:

```python
is_leap_year(2018) # false
is_leap_year(2017) # false
is_leap_year(2016) # true
```

La multiplicidad se puede comprobar así:

```python
# % - devuelve el resto de la división del operando izquierdo entre el derecho
# Comprobamos que number es múltiplo de 10
number % 10 == 0

# Comprobamos que number no es múltiplo de 10
number % 10 != 0
```
