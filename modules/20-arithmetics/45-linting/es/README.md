Cuando distintos desarrolladores escriben código con estilos distintos, el código se vuelve difícil de leer: en un sitio hay un espacio de más, en otro las sangrías son diferentes. Para evitar discrepancias, los programadores acordaron respetar un estilo de codificación único. Ese conjunto de reglas describe cómo debe verse el código: la colocación de los espacios, el formato de las funciones y los nombres de las variables.

Un estilo único significa código igualmente claro para todos los miembros del equipo, independientemente de quién lo haya escrito. Eso ahorra tiempo, reduce la cantidad de errores y simplifica el trabajo conjunto.

## Estándares de codificación

En el lenguaje Python hay un estilo de codificación oficial: el documento PEP8. Describe en detalle cómo dar formato al código: qué sangrías usar, cómo colocar los espacios, de qué longitud deben ser las líneas, cómo nombrar las variables y mucho más.

Ese estándar lo conocen y lo usan todos los desarrolladores de Python. A los principiantes les resulta útil consultarlo de vez en cuando y adquirir los hábitos correctos desde el principio. Sin embargo, no hace falta memorizarlo todo de golpe.

## Linters: comprobación automática del código

No hace falta memorizar todas las reglas a mano. Existen programas especiales que lo hacen por ti. Se llaman linters.

Un linter es una herramienta que analiza tu código e informa de las violaciones de los estándares.
Ayuda a:

- Deshacerse de los espacios de más
- Respetar las sangrías
- Escribir expresiones legibles y elegantes

## Un linter moderno: Ruff

A día de hoy, el linter más rápido y popular del mundo Python se considera Ruff. Reúne en sí las reglas de muchas otras herramientas: flake8, isort, pylint, black y otras. Ruff funciona rápido, admite la sintaxis moderna y se desarrolla activamente.

Veamos un ejemplo:

```python
result = 1 + 3
```

Ese código se ve descuidado, y el linter señalará el error con razón. Así se ve el proceso de comprobación:

```text
Código          Linter            Resultado
┌──────────┐    ┌──────────┐    ┌─────────────────┐
│ result=  │ →  │   Ruff   │ →  │ E225: missing   │
│  1+ 3    │    │          │    │ whitespace       │
└──────────┘    └──────────┘    └─────────────────┘
```

```text
E225: missing whitespace around operator
```

Eso significa que antes y después del + faltan espacios. Según el estándar, debería ser así:

```python
result = 1 + 3
```

## Las reglas y su sentido

Cada mensaje del linter está ligado a una regla concreta. Por ejemplo, E225 se refiere a los espacios, E302 se refiere a las líneas vacías antes de las funciones, y E501 se refiere a la longitud de las líneas. Cuando acabas de empezar, esos detalles pueden parecer poco importantes. Pero con el tiempo queda claro que son precisamente ellos los que forman un estilo único y legible.

La lista completa de reglas de Ruff se puede consultar en la [documentación oficial](https://docs.astral.sh/ruff/rules/).

## Usar el linter en tus propios proyectos

Cuando empieces a escribir tus propios proyectos fuera de la plataforma educativa, el linter será un ayudante imprescindible. Se puede configurar en cualquier editor de código, ejecutar en la terminal o conectar a la construcción del proyecto. El linter muestra los errores y sabe corregirlos automáticamente.
