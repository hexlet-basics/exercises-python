
La agregación de cadenas es cuando no se sabe de antemano qué contienen las cadenas y cuál es su tamaño.

Imagina una función que pueda multiplicar una cadena, repitiéndola un número fijo o determinado de veces:

```python
repeat('hexlet', 3)  # 'hexlethexlethexlet'
```

El principio de funcionamiento de esta función es que en un bucle se va "acumulando" la cadena un número determinado de veces:

```python
def repeat(text, times):
    # El elemento neutro para las cadenas es una cadena vacía
    result = ''
    i = 1

    while i <= times:
        # En cada iteración, se agrega la cadena al resultado
        result = result + text
        i = i + 1

    return result
```

https://replit.com/@hexlet/python-basics-loops-aggregation-strings

Veamos cómo se ejecuta este código paso a paso:

```python
# Para llamar a repeat('hexlet', 3)
result = ''
result = result + 'hexlet'  # hexlet
result = result + 'hexlet'  # hexlethexlet
result = result + 'hexlet'  # hexlethexlethexlet
```
