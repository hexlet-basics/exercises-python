
Ahora vamos a modificar la función del tema anterior para que no solo devuelva el tipo de oración, sino toda la cadena "La oración es normal" o "La oración es una pregunta":

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    else:
        sentence_type = 'normal'

    return "Sentence is " + sentence_type

print(get_type_of_sentence('Hodor'))   # => 'Sentence is normal'
print(get_type_of_sentence('Hodor?'))  # => 'Sentence is question'
```


Hemos añadido un `else` y un nuevo bloque. Se ejecutará si la condición en el `if` es falsa. También se pueden anidar otras condiciones `if` dentro del bloque `else`. "Else" se traduce como "en otro caso" o "de lo contrario".

Ejemplo de bloques anidados:

```python
number = 10

if number > 10:
    print("Number is greater than 10")
else:
    if number == 10:
        print("Number is exactly 10")
    else:
        print("Number is less than 10")
```

Se pueden estructurar las construcciones `if-else` de dos formas. Usando la negación se puede cambiar el orden de los bloques:

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char != '?':
        sentence_type = 'normal'
    else:
        sentence_type = 'question'

    return "Sentence is " + sentence_type
```

Para facilitar la estructura de la construcción, intenta elegir una comprobación sin negación y ajusta el contenido de los bloques en consecuencia.
