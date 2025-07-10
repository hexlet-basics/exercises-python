
En esta lección aprenderás que con las estructuras condicionales puedes cambiar el comportamiento de un programa dependiendo de las condiciones que se evalúen. Esto te permitirá escribir programas complejos que se comporten de manera diferente según la situación.

Como ejemplo, consideremos una función que determina el tipo de una oración dada. Al principio, esta distinguirá entre oraciones normales y preguntas:

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    if last_char == '?':
        return 'question'
    return 'normal'

print(get_type_of_sentence('Hodor'))   # => normal
print(get_type_of_sentence('Hodor?'))  # => pregunta
```


`if` es una estructura del lenguaje que controla el orden de ejecución de las instrucciones. Después de la palabra `if`, se le pasa una expresión booleana y se coloca dos puntos al final. Luego se describe un bloque de código. Este se ejecutará si el predicado es verdadero.

Si el predicado es falso, se omitirá el bloque de código y la función continuará su ejecución. En nuestro caso, la siguiente línea de código, `return 'normal'`, hará que la función devuelva la cadena y termine.

`return` puede estar en cualquier lugar de la función, incluso dentro de un bloque de código con una condición.
