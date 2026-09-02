Las funciones, en cualquier lenguaje de programación, tienen propiedades fundamentales. Esas propiedades ayudan a entender cómo se comportará la función en distintas situaciones, cómo probarla y dónde aplicarla. Una de esas propiedades es el **determinismo**.

Una **función determinista** devuelve siempre el mismo resultado con los mismos datos de entrada. Por ejemplo, determinista se puede llamar a la función que cuenta la cantidad de caracteres:

```python
len("hexlet")  # 6
len("hexlet")  # 6

len("wow")  # 3
len("wow")  # 3
```

A la función `len()` se la puede llamar infinitamente con el mismo argumento, y siempre devolverá el mismo resultado.

## Funciones no deterministas

Al tipo opuesto pertenecen las **funciones no deterministas**. Pueden devolver resultados distintos con los mismos datos de entrada o sin ellos (funciones sin parámetros). Un buen ejemplo es la función que devuelve un número aleatorio:

```python
# La sintaxis de las importaciones se estudiará más adelante
from random import random

# Función que devuelve un número aleatorio
random()  # 0.09856613113197676
random()  # 0.8839904367241888
```

Esa función no tiene argumentos, pero su resultado es distinto cada vez. Si al menos una llamada entre millones da otro resultado, la función se considera no determinista.

```text
Determinista:            No determinista:
len('abc') → siempre 3  random() → 0.42
len('abc') → siempre 3  random() → 0.91
len('abc') → siempre 3  random() → 0.07
```

## Por qué esto importa

El determinismo influye en cómo trabajamos con las funciones.

- las funciones deterministas son fáciles de probar y de predecir;
- son más simples de optimizar y de reutilizar;
- las funciones no deterministas son más difíciles de comprobar, porque el resultado cambia.

Por eso, allí donde sea posible, es mejor aspirar a que la función sea determinista.
