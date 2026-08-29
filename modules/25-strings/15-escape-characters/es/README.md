Supongamos que queremos mostrar el texto de abajo en dos líneas.

```text
- Are you hungry?
- Aaaarrrgh!
```

Si simplemente pasamos ese texto a `print()`, Python lo imprimirá todo en una sola línea. Técnicamente se pueden escribir dos `print()` seguidos, pero imaginemos que queremos hacerlo con uno solo.

```python
print("- Are you hungry?- Aaaarrrgh!")
# => - Are you hungry?- Aaaarrrgh!
```

Para que cada una empiece en una línea nueva, hay que añadir un salto de línea, es decir, «pulsar Enter». En programación eso se implementa añadiendo caracteres especiales, en este caso `\n`. Sí, no es un error tipográfico. A pesar de que aquí vemos dos caracteres, desde el punto de vista de Python es un solo carácter.

```python
print("- Are you hungry?\n- Aaaarrrgh!")
```

El resultado será este.

```text
- Are you hungry?
- Aaaarrrgh!
```

## ¿Qué es `\n`?

`\n` es una secuencia de control (en inglés escape sequence, a veces se dice «secuencia escapada»). Denota un salto de línea, pero no se muestra directamente. No verás `\n` en la salida del programa, ya que solo influye en la disposición del texto.

En los editores de texto, al pulsar Enter se añade el carácter invisible LF (Line Feed). Eso es justamente lo que significa `\n`. A veces se pueden ver esos caracteres si se activa la visualización de caracteres especiales.

```text
- ¡Hola!¶
- ¡Ah, hola!¶
- ¿Cómo estás?
```

Las impresoras, los editores y los intérpretes de Python entienden `\n` como la orden de empezar el texto en una línea nueva.

## Ejemplos de uso de `\n`

Así procesa Python la secuencia de control `\n`.

```text
En el código  'Hello\nWorld'
                    ↓
En pantalla   Hello
              World
```

La posición de `\n` cambia la salida final.

```python
print("Hello\nWorld")
# Hello
# World

print("Hello \nWorld")
# Hello
# World  (al final de la primera línea hay un espacio)

print("Hello\n World")
# Hello
#  World  (en la segunda línea hay un espacio al principio)

print("Hello\n\nWorld")
# Hello
#
# World  (una línea vacía entre ellas)
```

Los espacios antes o después de `\n` también se cuentan. Python los percibe como caracteres normales y los muestra en la salida.

También puedes insertar `\n` en cualquier parte de la cadena: antes, después o incluso usarlo por separado.

```python
print("First line")
print("\n")  # Simplemente una línea vacía
print("Second line")
```

El resultado será este.

```text
First line

Second line
```

## Cómo mostrar el propio carácter `\n`

`\n` en Python es una secuencia de control. Controla la disposición del texto y no se muestra en la pantalla como los caracteres normales. Si necesitas mostrar precisamente los caracteres `\` y `n`, y no un salto de línea, hay que escaparlos. Para eso, antes de la barra invertida se añade otra barra.

```python
print("Hello\\nWorld")
# Hello\nWorld

# Si se olvida indicar la segunda barra
print("Hello\nWorld")
# Hello
# World
```

En ese caso Python entiende `\\` como una barra invertida normal y muestra la cadena sin salto de línea.

## Otras secuencias de control

Además de `\n`, en Python hay otras secuencias de control.

- `\t` denota la tabulación (el equivalente de la tecla Tab).
- `\r` denota el retorno de carro (se usa en Windows, pero se aplica raramente en código Python).
- En programación se usa con más frecuencia precisamente `\n`, y basta para la mayoría de las tareas.

## Detalles importantes

- `\n` es un solo carácter, a pesar de que en el código se escribe como dos (\ y n).
- En Windows se usa por defecto la combinación `\r\n`, pero en Python (y en general en el desarrollo multiplataforma) se acostumbra a usar solo `\n`, para evitar problemas al llevar el código entre sistemas.
