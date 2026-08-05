Con los bucles se procesan números y se trabaja con cadenas. Por ejemplo, se puede obtener un carácter concreto por su índice y también formar cadenas en bucles.

Abajo hay un ejemplo de código que imprime las letras de cada palabra en una línea aparte:

```python
def print_name_by_symbol(name: str) -> None:
    i = 0
    # Esa comprobación se ejecutará hasta el final de la cadena,
    # incluido el último carácter. Su índice es `length - 1`.
    while i < len(name):
        # Accedemos al carácter por su índice
        print(name[i])
        i = i + 1

name = 'Arya'
print_name_by_symbol(name)
# => 'A'
# => 'r'
# => 'y'
# => 'a'
```

El bucle recorre cada carácter de la cadena por turnos:

```text
'Arya'
 │ │ │ │
 A r y a
 ↓ ↓ ↓ ↓
cada carácter se procesa por turnos
```

En este código es importante poner correctamente la condición del `while`. Las dos variantes, `i < len(name)` e `i <= len(name) - 1`, llevarán al mismo resultado.

## Invertir una cadena

En lugar de imprimir se puede construir una cadena nueva. Por ejemplo, escribamos una función que invierte una cadena:

```python
def reverse_string(text: str) -> str:
    result = ''
    i = len(text) - 1
    while i >= 0:
        result = result + text[i]
        i = i - 1
    return result

print(reverse_string('Arya'))    # => ayrA
print(reverse_string('hexlet'))  # => telxeh
```

La variable `result` se inicializa con la cadena vacía como elemento neutro de la concatenación. El bucle empieza en el último índice (`len(text) - 1`), avanza hacia cero y termina cuando el índice se vuelve menor que cero. En cada paso se añade al resultado el carácter actual. Al final la cadena se construye en orden inverso.
