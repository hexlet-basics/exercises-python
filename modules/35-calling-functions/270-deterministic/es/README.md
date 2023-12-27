
Las funciones en cada lenguaje de programación tienen propiedades fundamentales. Estas propiedades ayudan a predecir el comportamiento de las funciones, las formas de probarlas y dónde utilizarlas. Una de estas propiedades es el determinismo.

Una función determinista devuelve el mismo resultado para los mismos parámetros de entrada. Por ejemplo, se puede considerar determinista una función que cuenta la cantidad de caracteres:

```python
len('hexlet')  # 6
len('hexlet')  # 6

len('wow')  # 3
len('wow')  # 3
```

Se puede ejecutar esta función infinitamente y pasarle el valor `'hexlet'` - siempre devolverá `6`.

Veamos ahora el caso contrario: las funciones no deterministas. Por ejemplo, una función que devuelve un número aleatorio pertenece a esta categoría: para una misma entrada, siempre obtendremos un resultado diferente. Si al menos una de cada millón de llamadas a la función devuelve un resultado diferente, se considera no determinista. Esto también se aplica cuando no se toman parámetros:

```python
# La sintaxis de las importaciones se estudiará más adelante en Hexlet
from random import random

# Función que devuelve un número aleatorio
random()  # 0.09856613113197676
random()  # 0.8839904367241888
```

El determinismo es una propiedad importante de una función, ya que afecta a muchos aspectos. Por ejemplo, las funciones deterministas son convenientes para trabajar, ya que son fáciles de optimizar y probar. Si es posible, es mejor hacer que una función sea determinista.
