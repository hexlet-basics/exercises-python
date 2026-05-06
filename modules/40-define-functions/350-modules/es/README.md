Un archivo Python con funciones y constantes se llama **módulo**. Se puede conectar a un programa usando la palabra clave `import` y usar código listo en lugar de escribirlo uno mismo.

Python incluye una biblioteca estándar con módulos que vienen con el lenguaje. Uno de los más utilizados es `math`, que proporciona funciones y constantes matemáticas.

## Cómo importar un módulo

El comando `import` al inicio del archivo hace que el contenido del módulo esté disponible:

```python
import math

print(math.floor(3.7))  # => 3
print(math.ceil(3.2))   # => 4
```

Después de importar, se accede a las funciones a través del nombre del módulo y un punto. `math.ceil(3.2)` llama a la función `ceil` del módulo `math`.

## Funciones del módulo math

`floor` redondea un número hacia abajo al entero más cercano, `ceil` lo redondea hacia arriba:

```python
import math

print(math.floor(7.9))  # => 7
print(math.ceil(7.1))   # => 8
print(math.ceil(7.0))   # => 7
```

La diferencia importa cuando el número no es entero. `floor(7.9)` da 7, no 8, porque 7 es el entero más cercano por debajo.

## Importar nombres específicos

Cuando solo se necesita una parte del módulo, se pueden importar nombres específicos:

```python
from math import ceil, floor

print(ceil(3.2))   # => 4
print(floor(3.7))  # => 3
```

Esto permite usar `ceil` y `floor` directamente, sin el prefijo `math.`. El resultado es el mismo que con `import math`.

## Usar un módulo dentro de una función

Un módulo importado está disponible en todo el archivo, incluido el cuerpo de las funciones:

```python
import math

def trips_needed(items: int, capacity: int) -> int:
    return math.ceil(items / capacity)

print(trips_needed(10, 3))  # => 4
```

La función `trips_needed` usa `math.ceil`. La línea `import math` al inicio del archivo hace esto posible.
