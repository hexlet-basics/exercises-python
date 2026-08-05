Mientras el programa es pequeño, todo el código se puede guardar en un solo archivo. Ese enfoque resulta cómodo para ejemplos simples y tareas pequeñas. Pero con el tiempo el programa empieza a crecer. Cuando hay mucho código, orientarse en un solo archivo se vuelve difícil. Y las aplicaciones reales constan de decenas de miles de líneas (como mínimo) y de cientos de archivos.

Para dividir el programa en partes lógicas separadas, en Python se usan los módulos. Un módulo es un archivo con código y la extensión `.py`. Y el lenguaje ofrece mecanismos para acceder a las funciones y las constantes de otros archivos.

Además, Python mismo se distribuye ya con un conjunto de módulos incorporados (built-in) que se pueden usar en el propio código. Uno de los módulos que se usan a menudo es `math`. En él se encuentran funciones y constantes matemáticas.

## Cómo conectar un módulo

La instrucción `import` al principio del archivo hace accesible el contenido del módulo:

```python
import math

print(math.floor(3.7))  # => 3
print(math.ceil(3.2))   # => 4
```

Después de la importación, a las funciones se accede a través del nombre del módulo y un punto. El nombre del módulo coincide con el nombre del archivo sin la extensión. `math.ceil(3.2)` llama a la función `ceil` del módulo `math`.

Desde el punto de vista técnico, un módulo en Python es un objeto. Por eso el acceso mediante el punto funciona igual que al acceder a los métodos o las propiedades de los objetos. Al mismo tiempo, el módulo sirve ante todo para organizar el código. Normalmente, dentro de un módulo se sitúan funciones, constantes y datos auxiliares relacionados por una tarea común.

## Funciones del módulo math

Analicemos algunas funciones de ese módulo. `floor()` redondea el número hacia abajo hasta el entero más cercano y `ceil()` redondea hacia arriba:

```python
import math

print(math.floor(7.9)) # => 7
print(math.ceil(7.1))  # => 8
print(math.ceil(7.0))  # => 7
```

La diferencia se nota cuando el número no es entero. `floor(7.9)` da 7 y no 8, porque 7 es el entero más cercano por debajo.

## Importación de nombres concretos

Cuando solo hace falta una parte del módulo, se pueden importar nombres concretos:

```python
from math import ceil, floor

print(ceil(3.2))   # => 4
print(floor(3.7))  # => 3
```

Esa importación permite acceder a `ceil` y `floor` directamente, sin el prefijo `math.`. El resultado es el mismo que con `import math`. Esa forma es cómoda cuando del módulo solo hacen falta unas pocas funciones. Pero si el módulo es grande o los nombres de las funciones son demasiado generales, normalmente se prefiere el `import` normal, para que quede claro de dónde salió exactamente la función.

## Un módulo dentro de una función

El módulo importado está disponible en todo el archivo, incluido el cuerpo de las funciones:

```python
import math

# Calcula la cantidad de viajes necesarios para transportar todos los objetos
def trips_needed(items: int, capacity: int) -> int:
    return math.ceil(items / capacity)

print(trips_needed(10, 3)) # => 4
```

## Conflictos de nombres

Los módulos ayudan a evitar los conflictos de nombres. En programas grandes, distintas partes del código pueden contener funciones o variables con los mismos nombres. Por ejemplo, en el programa puede existir ya una función `floor`, y el módulo `math` también contiene una función con ese nombre. Gracias a la división en módulos podemos crear tantas funciones con el mismo nombre como queramos; lo importante es que estén en archivos distintos. Y eso funciona incluso con las importaciones:

```python
import math

def floor(number):
    return "custom floor"

print(floor(3.7))       # => custom floor
print(math.floor(3.7))  # => 3
```

Gracias al nombre del módulo, Python entiende a qué función hay que llamar exactamente. Eso es especialmente importante al usar bibliotecas de terceros, porque distintos desarrolladores pueden elegir los mismos nombres para sus funciones.

Los problemas surgen más a menudo al importar nombres concretos. Por ejemplo, si en el archivo ya existe una función con el mismo nombre:

```python
from math import floor

def floor(number):
    return "custom floor"

print(floor(3.7))  # => custom floor
```

Después de definir la nueva función, el nombre `floor` empieza a referirse ya a ella. La función de `math` deja de estar accesible con ese nombre. Por esa razón, en muchos proyectos se prefiere el `import` normal, sobre todo en programas grandes y al trabajar con bibliotecas de terceros.
