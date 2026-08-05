Con el bucle `while` se resuelve cualquier tarea de recorrido de elementos, pero lo caracteriza su verbosidad. Para el `while` hay que fijar la condición de parada e introducir un contador. Cuando hay pocos bucles eso es normal, pero en el código real los bucles aparecen a cada paso. Por eso gestionar las condiciones a mano resulta fatigoso, sobre todo cuando la condición de parada es evidente.

Por ejemplo, si queremos recorrer los caracteres de una cadena, el ordenador puede entender por sí mismo cuándo termina la cadena. Para esas situaciones, en Python existe el bucle `for`. Él mismo sabe cuándo hay que detenerse: `for` trabaja con valores que se pueden recorrer elemento por elemento (por ejemplo, con una cadena).

Una cadena consta de caracteres, y el bucle `for` permite recorrer la cadena carácter a carácter. Un ejemplo:

```python
text = 'code'
for symbol in text:
    print(symbol)

# => c
# => o
# => d
# => e
```

En el código de arriba, `for` recorre cada carácter de la cadena, lo escribe en la variable `symbol` y llama al bloque interno de código, donde se usa esa variable. El nombre de esa variable puede ser cualquiera. La estructura general del bucle `for` se ve así: `for <variable> in <objeto que se puede recorrer>`.

Comparemos `for` y `while` para una misma tarea:

```text
for char in 'Hi!':     while i < len('Hi!'):
    print(char)            print(text[i])
                           i = i + 1
│                      │
└── más simple         └── hace falta un contador
```

Veamos cómo implementar la función de invertir una cadena con el bucle `for`. Esa tarea aparece en las entrevistas.

```python
def reverse_string(text: str) -> str:
    # Valor inicial
    result = ''
    # char - variable en la que se escribe el carácter actual
    for char in text:
        # Unimos en orden inverso
        result = char + result
    # El bucle termina cuando se ha recorrido toda la cadena
    return result


reverse_string('go!')  # => '!og'
```

Analicemos en detalle cómo se ejecuta el bucle del ejemplo de arriba en cada paso de las iteraciones.

```text
reverse_string('go!')

antes del bucle: result = ''

iteración 1: char = 'g'
result = char + result
       = 'g'  + ''
       = 'g'

iteración 2: char = 'o'
result = char + result
       = 'o'  + 'g'
       = 'og'

iteración 3: char = '!'
result = char + result
       = '!'  + 'og'
       = '!og'
```

Ahora contemos la cantidad de apariciones de un carácter en una cadena sin tener en cuenta el caso:

```python
# text - texto arbitrario
# char - carácter que hay que contar
def chars_count(text: str, char: str) -> int:
    # Como buscamos una suma, el valor inicial es 0
    result = 0
    for current_char in text:
        # pasamos todo a minúsculas,
        # para no depender del caso actual
        if current_char.lower() == char.lower():
            result += 1
    return result


chars_count('hexlet!', 'e')  # 2
chars_count('hExlet!', 'e')  # 2
chars_count('hExlet!', 'E')  # 2
chars_count('hexlet!', 'a')  # 0
```
