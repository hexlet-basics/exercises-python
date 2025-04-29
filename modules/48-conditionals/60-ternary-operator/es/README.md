
Eche un vistazo a la definición de una función que devuelve el módulo de un número dado:

```python
def abs(number):
    if number >= 0:
        return number
    return -number
```

Pero se puede escribir de manera más concisa. Para ello, a la derecha de `return` debe haber una expresión, pero `if` es una instrucción y no una expresión. En Python existe una construcción que funciona como un `if-else`, pero se considera una expresión. Se llama **operador ternario** y es el único operador en Python que requiere tres operandos:

```python
def abs(number):
    return number if number >= 0 else -number
```

El patrón general se ve así: `<expression on true> if <predicate> else <expression on false>`.

Vamos a reescribir la versión inicial de `get_type_of_sentence()` de manera similar.

Antes:

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    if last_char == '?':
        return 'question'
    return 'normal'
```

Después:

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    return 'question' if last_char == '?' else 'normal'

print(get_type_of_sentence('Hodor'))   # => normal
print(get_type_of_sentence('Hodor?'))  # => question
```


Se puede anidar un operador ternario dentro de otro operador ternario. Pero no se recomienda hacerlo, ya que ese código es difícil de leer y depurar.
