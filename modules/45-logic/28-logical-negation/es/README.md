Junto con los operadores lógicos **Y** y **O**, se usa a menudo la operación de "**negación**". Cambia el valor lógico por el contrario. En Python a la negación le corresponde el operador unario `not` (en otros lenguajes `!`):

```python
not True   # False
not False  # True
```

Por ejemplo, si hay una función que comprueba la paridad de un número, con la negación se puede hacer la comprobación de la imparidad:

```python
def is_even(number: int) -> bool:
    return number % 2 == 0

print(is_even(10))      # => True
print(not is_even(10))  # => False
```

En el ejemplo de arriba añadimos `not` a la izquierda de la llamada a la función y obtuvimos la acción inversa.

La negación permite expresar en el código las reglas pensadas sin escribir funciones nuevas. Si se escribe `not not is_even(10)`, el código funcionará incluso en ese caso:

```python
print(not not is_even(10))  # => True
```

En lógica, la doble negación equivale a la ausencia de negación:

```python
not not True   # True
not not False  # False

print(not not is_even(10))  # => True
print(not not is_even(11))  # => False
```

`not` se puede combinar con `and` y `or`. Entre los operadores lógicos tiene la prioridad más alta, por eso se aplica primero:

```python
not True or True    # (not True) or True   => False or True  => True
not True and False  # (not True) and False => False and False => False
```

Los paréntesis cambian el orden de evaluación:

```python
not (True or True)   # not True  => False
not (True and False) # not False => True
```

Un ejemplo práctico: una función comprueba si el conductor puede ponerse al volante; hacen falta el carnet y la sobriedad:

```python
def can_drive(has_license: bool, is_drunk: bool) -> bool:
    return has_license and not is_drunk

print(can_drive(True, False))   # => True  (tiene carnet, sobrio)
print(can_drive(True, True))    # => False (tiene carnet, pero ebrio)
print(can_drive(False, False))  # => False (no tiene carnet)
```

Ahora sabes qué significan los operadores **Y**, **O** y `not`. Con su ayuda podrás fijar condiciones compuestas de dos o más expresiones lógicas.

## Las leyes de De Morgan

Al trabajar con expresiones lógicas complejas, a veces hace falta invertirlas o reescribirlas en una forma equivalente que sea más fácil de leer. Para eso existen las **leyes de De Morgan**: dos reglas que describen cómo se distribuye la negación por una expresión compuesta:

```python
not (A and B)  ==  not A or not B
not (A or B)   ==  not A and not B
```

La primera ley: la negación de la conjunción es igual a la disyunción de las negaciones. Comprobémoslo:

```python
not (True and False)      # not False => True
not True or not False     # False or True => True
```

La segunda ley: la negación de la disyunción es igual a la conjunción de las negaciones:

```python
not (True or False)       # not True => False
not True and not False    # False and True => False
```

En la práctica, las leyes de De Morgan ayudan a simplificar las condiciones. Por ejemplo, en lugar de `not (is_admin or is_moderator)` se puede escribir `not is_admin and not is_moderator`, que se lee como "no es administrador y no es moderador".
