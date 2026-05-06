Los programas Python casi siempre usan código escrito por otros. Reinventar funciones matemáticas, manejo de fechas o peticiones de red no tiene sentido — todo esto ya está disponible. Python usa paquetes para compartir y reutilizar código.

Un paquete es un directorio de archivos Python organizados por tema. La biblioteca estándar de Python contiene decenas de estos paquetes, que cubren desde matemáticas hasta el acceso al sistema de archivos.

## Importar un paquete

Para usar código de un paquete, hay que importarlo con la palabra clave `import`. Veamos el paquete `math`:

```python
import math

print(math.sqrt(16))  # => 4.0
print(math.pi)        # => 3.141592653589793
```

Después de `import math`, todo el contenido del paquete está disponible con notación de punto: `math.sqrt`, `math.floor`, `math.pi`.

## Importar nombres específicos

Una sintaxis alternativa permite importar solo lo que se necesita:

```python
from math import sqrt, pi

print(sqrt(25))  # => 5.0
print(pi)        # => 3.141592653589793
```

Ahora `sqrt` y `pi` están disponibles directamente, sin el prefijo `math.`. La forma `import math` hace explícito el origen de la función, lo que ayuda al leer código desconocido. La forma `from math import` es cómoda cuando se necesitan pocas funciones concretas y escribir el prefijo cada vez resulta tedioso.

## Alias

La palabra clave `as` permite dar un alias a un nombre importado:

```python
from math import sqrt as sq

print(sq(9))  # => 3.0
```

Un alias es útil cuando un nombre entra en conflicto con una variable existente o es demasiado largo.

## Biblioteca estándar

Python viene con un conjunto amplio de paquetes integrados. Algunos de uso frecuente:

- `math` — funciones matemáticas: `sqrt`, `hypot`, `floor`, `ceil`, `pi`
- `random` — números aleatorios: `randint`, `choice`, `shuffle`
- `datetime` — trabajo con fechas y horas

```python
import random

print(random.randint(1, 6))                          # => número aleatorio entre 1 y 6
print(random.choice(['rock', 'paper', 'scissors']))  # => elemento aleatorio
```

## Paquetes de terceros

Más allá de la biblioteca estándar, existen miles de paquetes creados por desarrolladores de todo el mundo. Se instalan con `pip`, el gestor de paquetes de Python:

```bash
pip install requests
```

Después de la instalación, las importaciones funcionan igual que con los paquetes integrados.
