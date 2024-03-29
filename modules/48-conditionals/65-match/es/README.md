
Muchos lenguajes, además de la estructura condicional `if`, incluyen `switch`. Con la versión 3.10 de Python, se agregó el operador `match` con funcionalidad similar. En esta lección, aprenderemos sobre este operador.

El operador `match` es una versión especializada de `if` creada para situaciones específicas. Por ejemplo, se debe utilizar cuando hay una cadena de `if else` con comprobaciones de igualdad:

```python
if status == 'processing':
    # Hacer algo
elif status == 'paid':
    # Hacer algo más
elif status == 'new':
    # Hacer algo diferente
else:
    # Hacer algo más
```

Esta comprobación compuesta tiene una característica distintiva: cada rama es una comprobación del valor de la variable `status`. El operador `match` permite escribir este código de forma más corta y expresiva:

```python
match status:
    case 'processing':  # status == 'processing'
        # Hacer algo
    case 'paid':  # status == 'paid'
        # Hacer algo más
    case 'new':  # status == 'new'
        # Hacer algo diferente
    case _:  # else
        # Hacer algo más
```

En términos de cantidad de elementos, `match` es una construcción compleja. Está compuesta por los siguientes elementos:

* Una descripción externa que incluye la palabra clave `match`. Esta es la variable cuyos valores determinarán el comportamiento del `match`.
* Las construcciones `case`, dentro de las cuales se describe el comportamiento para diferentes valores de la variable considerada. Cada `case` corresponde a un `if` en el ejemplo anterior. Además, `case _` es una situación especial que corresponde a la rama `else` en las estructuras condicionales. Al igual que `else`, no es obligatorio especificar `case _`.

Dentro de `match`, solo se permite la sintaxis mostrada anteriormente. En otras palabras, se pueden utilizar `case`. Sin embargo, dentro de cada `case`, la situación es diferente. Aquí se puede ejecutar cualquier código arbitrario:

```python
match count:
    case 1:
        # Hacer algo útil
    case 2:
        # Hacer algo útil
    case _:
        # Hacer algo
```

A veces, el resultado obtenido dentro de `case` es el final de la ejecución de la función que contiene el `match`. En ese caso, es necesario devolverlo de alguna manera. Hay dos formas de resolver este problema:

Primera forma: crear una variable antes del `match`, asignarle un valor dentro de `case` y luego devolver el valor de esa variable al final:

```python
def count_items(count):
    # Declarar una variable
    result = ''

    # Llenar el espacio
    match count:
        case 1:
            result = 'one'
        case 2:
            result = 'two'
        case _:
            result = None

    # Devolver el valor
    return result
```

La segunda forma es más simple y corta. En lugar de crear una variable al trabajar con `case`, se puede hacer un retorno normal de la función:

```python
def count_items(count):
    match count:
        case 1:
            return 'one'
        case 2:
            return 'two'
        case _:
            return None
```

Aunque el operador `match` se encuentra en el código, técnicamente siempre se puede prescindir de él. La ventaja clave de su uso es que expresa mejor la intención del programador cuando se necesitan comprobar valores específicos de una variable. Aunque el código es un poco más largo físicamente, es más fácil de leer en comparación con los bloques `elif`.
