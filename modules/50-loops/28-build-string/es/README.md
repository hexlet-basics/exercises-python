
Los bucles también se pueden utilizar para formar cadenas. Este tipo de tarea es común en la programación web. Se reduce a una simple agregación, ya sea mediante interpolación o concatenación.

La inversión de una cadena es un problema algorítmico que se plantea en las entrevistas. La forma correcta de invertir una cadena es utilizar una función de la biblioteca estándar. Sin embargo, es importante saber cómo implementarla.

Uno de los algoritmos se ve así:

1. Construimos una nueva cadena.

2. Recorremos los caracteres de la cadena original en orden inverso.

```python
def reverse_string(string):
    index = len(string) - 1
    reversed_string = ''

    while index >= 0:
        current_char = string[index]
        reversed_string = reversed_string + current_char
        # Lo mismo ocurre usando la interpolación
        # reversed_string = f'{reversed_string}{current_char}'
        index = index - 1

    return reversed_string

reverse_string('Game Of Thrones')  # 'senorhT fO emaG'
# Comprobación del elemento neutro
reverse_string('')  # ''
```

Vamos a analizar la función línea por línea:

* `index = len(string) - 1` — guardamos en una nueva variable el índice del último carácter de la cadena (los índices comienzan en cero).
* `reversed_string = ''` — inicializamos una cadena donde se guardará el resultado.
* `while index >= 0:` — condición: repetimos el cuerpo del bucle mientras el índice actual no llegue a `0`, es decir, hasta el primer carácter.
* `current_char = string[index]` — tomamos el carácter de la cadena según el índice actual.
* `reversed_string = reversed_string + current_char` — añadimos al resultado el nuevo valor: la cadena resultado actual más el nuevo carácter.
* `index = index - 1` — actualizamos el contador.
* `return reversed_string` — cuando el bucle termina, devolvemos la cadena resultado.

Al trabajar con cadenas, los programadores a menudo cometen un error: salirse de los límites de la cadena. Si el valor inicial del contador no se elige correctamente o se comete un error en el predicado del bucle, la función puede acceder a un carácter inexistente.

A menudo se olvida que el índice del último elemento siempre es menor en uno que el tamaño de la cadena. En las cadenas, el índice inicial es `0`, lo que significa que el índice del último elemento es `len(str) - 1`.
