Imaginemos que tenemos una cadena y queremos reemplazar en ella un carácter, por ejemplo la primera letra del nombre:

```python
first_name = "Alexander"
first_name[0] = "B"  #
```

Python lanzará un error de inmediato:

```text
TypeError: 'str' object does not support item assignment
```

¿Qué significa? Las cadenas en Python no se pueden modificar por partes. Una vez creadas, pasan a ser inmutables (o, como dicen los programadores, inmutables por diseño).

## ¿Por qué las cadenas son inmutables?

Python está hecho de tal manera que los tipos primitivos (cadenas, números, valores booleanos) no se pueden modificar. Eso aporta ventajas importantes:

- Seguridad: los valores no se modificarán por accidente
- Rendimiento: con objetos inmutables es más fácil trabajar dentro del intérprete
- Previsibilidad: hay menos efectos inesperados al pasar los datos a las funciones

## ¿Y cómo se modifica entonces una cadena?

Si hace falta "modificar" una cadena, se crea una cadena nueva y se guarda en la misma variable:

```python
first_name = "Alexander"
first_name = "Blexander"

print(first_name)  # => Blexander
```

La variable first_name ahora simplemente apunta a otra cadena. Se produce un reemplazo del valor de la variable, y la cadena en sí queda intacta.

```text
name = 'Alexander'

name[0] = 'B'  →  ¡Error! Las cadenas son inmutables.

name = 'B' + name[1:]
└─────────┬──────────┘
     'Blexander'       ←  se creó una cadena nueva
```

## ¿Una variable nueva o la misma?

Reutilizar una variable solo vale la pena cuando se trata de una misma entidad. Si el usuario introdujo un nombre nuevo, esa es ya otra entidad, y es mejor crear una variable aparte:

```python
# Una misma cadena, simplemente la actualizamos
name = "Alexander"
name = "Blexander"

# Entidades distintas, mejor variables distintas
first_name = "Alexander"
corrected_first_name = "Blexander"
```

Intentar "meter" todas las cadenas en una sola variable enreda el código. La variable deja de decir qué se guarda en ella.

## Conclusión

Los tipos de datos primitivos en Python (las cadenas str, los números enteros int, los números reales float y los valores lógicos bool) son inmutables (immutable). Eso significa que, una vez creados, su valor interno no se puede modificar. Cambiar un carácter de una cadena o un dígito de un número es imposible: cualquier "modificación" ocurre creando un valor nuevo y redefiniendo la variable.
