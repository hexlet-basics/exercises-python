
Queremos mostrar el siguiente diálogo:

```text
- Are you hungry?
- Aaaarrrgh!
```

Intentemos imprimir en pantalla una cadena de texto con este contenido:

 ```python
print("- Are you hungry?- Aaaarrrgh!")
# => - Are you hungry?- Aaaarrrgh!
```

Como puedes ver, el resultado no es el que esperábamos. Las cadenas de texto se han colocado una al lado de la otra en lugar de una debajo de la otra. Necesitamos decirle al intérprete "presiona Enter" - y que haga un salto de línea después del signo de interrogación. Esto se puede hacer utilizando el carácter `\n`:

```python
print("- Are you hungry?\n- Aaaarrrgh!")
# => - Are you hungry?
# => - Aaaarrrgh!
```

`\n` es un ejemplo de una **secuencia de escape**. Estas secuencias también se conocen como construcciones de control. No se pueden ver en la forma en que se escriben.

Cuando escribes algún texto en Word, presionas Enter al final de la línea. El editor agrega un carácter especial invisible al final de la línea, que se llama LINE FEED (LF, salto de línea). En algunos editores incluso puedes habilitar la visualización de caracteres invisibles. Entonces el texto se verá más o menos así:

```text
- ¡Hola!¶
- ¡Oh, hola!¶
- ¿Cómo estás?
```

El dispositivo que muestra el texto correspondiente tiene en cuenta este carácter. Por ejemplo, una impresora, al encontrar un LF, avanza el papel hacia arriba una línea, y un editor de texto mueve todo el texto siguiente hacia abajo, también una línea.

Hay varias docenas de estos caracteres invisibles, pero en programación sólo se encuentran algunos. Además del salto de línea, estos caracteres incluyen:

* tabulación `\t` - la ruptura que se produce al presionar la tecla Tab
* retorno de carro `\r` - solo funciona en Windows

Puedes reconocer estas construcciones de control en el texto por el carácter `\`. Los programadores a menudo usan el salto de línea `\n` para formatear correctamente el texto. Por ejemplo, escribamos este código:

```python
print("Gregor Clegane\nDunsen\nPolliver\nChiswyck")
```

Entonces se mostrará en pantalla:

```text
Gregor Clegane
Dunsen
Polliver
Chiswyck
```

Al trabajar con el carácter de salto de línea, ten en cuenta los siguientes puntos:

1. No importa lo que haya antes o después de `\n`: un carácter o una cadena vacía. El salto se detectará y se realizará de todos modos.

2. Una cadena puede contener solo `\n`:

  ```python
  print('Gregor Clegane') # Cadena de texto
  print("\n") # Cadena con un carácter de salto de línea invisible
  print('Dunsen') # Cadena de texto
  ```

  El programa mostrará en pantalla:

  ```text
  Gregor Clegane


  Dunsen
  ```

3. En el código, la secuencia `\n` se ve como dos caracteres, pero para el intérprete es un solo carácter especial.

4. Si deseas mostrar `\n` como texto (dos caracteres separados), puedes usar la técnica de escape: agregar otro `\` al principio. La secuencia `\\n` se mostrará como los caracteres `\` y `n`, que van uno tras otro:

```python
print("Joffrey loves using \\n")
# => Joffrey loves using \n
```

En Windows, por defecto se utiliza `\r\n` para los saltos de línea. Esta combinación funciona bien solo en Windows, pero causa problemas al transferir a otros sistemas. Por ejemplo, cuando en un equipo de desarrollo hay usuarios de Linux.

El problema es que la secuencia `\r\n` se interpreta de manera diferente según la codificación seleccionada, de lo cual hablaremos más adelante. Por esta razón, en entornos de desarrollo se recomienda siempre usar `\n` sin `\r`.

En este caso, el salto de línea siempre se interpreta de la misma manera y funciona perfectamente en cualquier sistema. No olvides configurar tu editor para usar `\n`.
