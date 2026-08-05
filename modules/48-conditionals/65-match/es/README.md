El operador `match` es una versión especializada de `if`, creada para situaciones particulares. Por ejemplo, hay que usarla allí donde hay una cadena de `if else` con comprobaciones de igualdad:

```python
if status == 'processing':
    # Hacemos una cosa
elif status == 'paid':
    # Hacemos otra
elif status == 'new':
    # Hacemos una tercera
else:
    # Hacemos una cuarta
```

Esa comprobación compuesta tiene un rasgo distintivo. Cada rama aquí es una comprobación del valor de la variable `status`. El operador `match` permite escribir ese código de forma más corta y expresiva.

```python
match status:
    case 'processing':  # status == 'processing'
        # Hacemos una cosa
    case 'paid':  # status == 'paid'
        # Hacemos otra
    case 'new':  # status == 'new'
        # Hacemos una tercera
    case _:  # else
        # Hacemos una cuarta
```

```text
match valor:
  │
  ├── case 'a' → bloque 1
  ├── case 'b' → bloque 2
  ├── case 'c' → bloque 3
  └── case _   → bloque por defecto
```

Desde el punto de vista de la cantidad de elementos, `match` es una construcción compleja. La descripción externa incluye la palabra clave `match` y la variable según cuyos valores `match` elegirá el comportamiento. Dentro se sitúan las construcciones `case`, cada una de las cuales describe el comportamiento para uno de los valores de la variable. Cada `case` corresponde a un `if` del ejemplo de arriba. Además, `case _` es una situación especial que corresponde a la rama `else` de las construcciones condicionales. Igual que `else`, indicar `case _` no es obligatorio.

Dentro de `match` solo se admite la sintaxis mostrada arriba. En otras palabras, allí se puede usar `case`. Pero dentro de cada `case` la situación es distinta. Aquí se puede ejecutar cualquier código arbitrario.

```python
match count:
    case 1:
        # Hacemos algo útil
    case 2:
        # Hacemos algo útil
    case _:
        # Hacemos algo
```

A veces el resultado obtenido dentro de un `case` termina la ejecución de la función que contiene el `match`. En ese caso hay que devolverlo de alguna manera hacia fuera. Para resolver esa tarea hay dos formas.

La primera. Crear una variable antes del `match`, rellenarla en el `case` y luego, al final, devolver el valor de esa variable hacia fuera.

```python
def count_items(count):
    # Declaramos la variable
    result = ''

    # La rellenamos
    match count:
        case 1:
            result = 'one'
        case 2:
            result = 'two'
        case _:
            result = None

    # La devolvemos
    return result
```

La segunda forma es más simple y más corta. En lugar de crear una variable, al trabajar con `case` se puede hacer un retorno normal desde la función.

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

El operador `match`, aunque aparece en el código, técnicamente siempre se puede evitar. La utilidad clave de usarlo está en que expresa mejor la intención del programador cuando hay que comprobar valores concretos de una variable. Aunque el código haya crecido físicamente un poco, es más fácil de leer, a diferencia de los bloques `elif`.
