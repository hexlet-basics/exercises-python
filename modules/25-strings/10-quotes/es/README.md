Las cadenas en la programación en Python se usan con mucha frecuencia y en las situaciones más diversas. Con ellas trabajamos con texto, mostramos mensajes en la pantalla, procesamos la entrada del usuario e interactuamos con sistemas externos.

Desde el punto de vista de Python, una cadena es simplemente un conjunto de caracteres encerrado entre comillas. Veamos unos ejemplos.

```python
"Hello"

"Goodbye"
"G"
" "
""
```

Todas esas variantes son cadenas.

- `'Hello'`, `'Goodbye'` y `'G'` son cadenas de varios caracteres o de uno solo.
- `' '` es una cadena formada por un solo espacio.
- `''` es una cadena vacía, en ella no hay ni un carácter. Cumple el mismo papel que el 0 en matemáticas.

Es decir, todo lo que está dentro de las comillas se considera una cadena, aunque solo haya un espacio o no haya absolutamente nada.

Si se muestran las cadenas en la pantalla, `'Hello'` y `'Goodbye'` se verán con claridad. Pero `' '` y `''` pueden despistar, porque la salida de una cadena vacía parece una ausencia total, mientras que una cadena con un espacio muestra un «espacio vacío» que visualmente es difícil de distinguir. Sin embargo, Python las diferencia con claridad. Una cadena vacía significa la ausencia de caracteres, mientras que una cadena con un espacio contiene un carácter de espacio concreto.

Pregunta de control. ¿Son estas cadenas iguales o no?

```python
"hexlet"

" hexlet"
```

## Terminología. ¿Cadena o línea?

En programación hay una trampa terminológica.

- Una cadena (string) es un tipo de dato (el que analizamos arriba), por ejemplo 'hello'.
- Una línea (line) es una fila de texto en un archivo o en el código.

Por ejemplo, en el código de abajo hay una línea, pero no una cadena.

```python
print(5)
```

Para evitar la confusión, en este curso usaremos estas formulaciones.

- Cadena, cuando hablamos del tipo de dato.
- Línea, cuando se trata de las filas del código.

## Comillas simples y dobles

En Python las cadenas se pueden escribir tanto entre comillas simples como entre dobles.

```python
print("Hello")
print("Hello")
```

Por defecto se acostumbra a usar comillas simples `'`, si dentro de la cadena no se necesitan dobles. Ese estilo lo sigue el estándar oficial de formato de código _PEP8_.

## El problema de las comillas dentro de la cadena

Imagina que quieres imprimir la cadena _Dragon's mother_. En ella hay un apóstrofo (_'s_) que coincide con el carácter de comilla simple. Probemos así.

```python
print('Dragon's mother')
# SyntaxError: invalid syntax
```

Python decidirá que la cadena termina después de la palabra 'Dragon', y el resto no lo reconocerá como código válido, lo que provocará un error de sintaxis. Para evitarlo, envolvemos la cadena en comillas dobles.

```python
print("Dragon's mother")
```

Ahora Python entiende que la comilla simple dentro de la cadena es un carácter normal, y que la cadena en sí empieza y termina con comillas dobles.

Si dentro de la cadena hacen falta comillas dobles y por fuera simples, tampoco habrá problemas.

```python
print('He said "No"')
```

A veces en la cadena aparecen los dos tipos de comillas.

```python
Dragon's mother said "No"
```

En ese caso, para que Python no confunda las comillas de dentro de la cadena con las exteriores, se usa el carácter de escape, la barra invertida `\`. Le dice al intérprete que el carácter que la sigue es parte de la cadena y no un carácter de control.

```python
print('Dragon\'s mother said "No"')
# => Dragon's mother said "No"
```

Aquí escapamos las comillas dobles dentro de la cadena encerrada en comillas dobles.

Fíjate: Python percibe `\"` como un solo carácter de comilla, no como dos caracteres.
Lo mismo ocurre con `\'`, `\\`, `\n` y otras secuencias de control. Se ven como dos caracteres en el código, pero en la cadena cuentan como uno.

Lo mismo funciona en el caso contrario.

```python
print('Dragon\'s mother said "No"')
# => Dragon's mother said "No"
```

## Cómo mostrar la barra invertida

Para mostrar la barra invertida en sí, también hay que escaparla.

```python
print("\\")
# => \
```
