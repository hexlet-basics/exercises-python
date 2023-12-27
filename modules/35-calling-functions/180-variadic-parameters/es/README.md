
En esta lección vamos a analizar la función `max()`, y veremos cómo funciona en Python.

Algunas funciones tienen la particularidad de aceptar un número variable de parámetros. Y no nos referimos a los valores por defecto. Mira este ejemplo:

```python
max(1, 10, 3)  # 10
```

En el ejemplo anterior, la función `max()` encuentra el valor máximo entre los parámetros proporcionados. Para saber cuántos parámetros se pueden pasar como entrada, debemos consultar la [documentación](https://docs.python.org/3/library/functions.html?highlight=pow#max) de esta función. Allí veremos esta construcción:

```
max(arg1, arg2, *args[, key])
```

Esto significa que `max()` acepta dos o más parámetros:

```python
max(1, -3, 2, 3, 2)  # 3
```

Si la función encuentra varios parámetros con el valor máximo, devolverá el primero de estos.
