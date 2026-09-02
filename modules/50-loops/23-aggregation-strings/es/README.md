La agregación de cadenas reúne las tareas en las que no se sabe de antemano qué contienen las cadenas ni cuál es su tamaño.

Imaginemos una función que repite una cadena la cantidad indicada de veces. Sí, en Python está incorporado para la repetición el operador de multiplicar una cadena por un número, pero aquí veremos cómo está implementado aproximadamente por dentro:

```python
repeat("hexlet", 3)  # 'hexlethexlethexlet'
```

La función va aumentando la cadena en un bucle la cantidad indicada de veces:

```python
def repeat(text: str, times: int) -> str:
    # El elemento neutro de las cadenas es la cadena vacía
    result = ""
    i = 1

    while i <= times:
        # Cada vez añadimos la cadena al resultado
        result = result + text
        i = i + 1

    return result
```

Describamos la ejecución de ese código paso a paso.

```python
# Para la llamada repeat('hexlet', 3)
result = ""
result = result + "hexlet"  # hexlet
result = result + "hexlet"  # hexlethexlet
result = result + "hexlet"  # hexlethexlethexlet
```

De forma visual, el proceso de crecimiento de la cadena se ve así.

```text
repeat('hexlet', 3):

i=1: result = ''             + 'hexlet' = 'hexlet'
i=2: result = 'hexlet'       + 'hexlet' = 'hexlethexlet'
i=3: result = 'hexlethexlet' + 'hexlet' = 'hexlethexlethexlet'
                                            └── resultado
```

## El elemento neutro

Para que el crecimiento funcione hace falta un valor de partida. Para las cadenas, ese valor es la **cadena vacía** `''`.

Se llama elemento neutro porque en la concatenación no cambia nada:

```python
print("" + "abc")  # => abc
print("abc" + "")  # => abc
```

Por eso es precisamente la cadena vacía la que se usa siempre como valor inicial en la agregación de cadenas.
