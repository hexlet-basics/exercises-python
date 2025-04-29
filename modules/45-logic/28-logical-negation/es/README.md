
Junto con los operadores lógicos **Y** y **O**, a menudo se utiliza la operación de "**negación**". Esta operación cambia el valor lógico al opuesto. En programación, la negación se representa con el operador unario `not`:

```python
not True   # False
not False  # True
```

Por ejemplo, si tenemos una función que verifica si un número es par, podemos utilizar la negación para verificar si es impar:

```python
def is_even(number):
    return number % 2 == 0

print(is_even(10))      # => True
print(not is_even(10))  # => False
```

En el ejemplo anterior, agregamos `not` antes de llamar a la función y obtuvimos el resultado opuesto.

La negación es una herramienta que nos permite expresar reglas deseadas en el código sin tener que escribir nuevas funciones.

Incluso si escribimos `not not is_even`, el código funcionará de la siguiente manera:

```python
print(not not is_even(10))  # => True
```


En lógica, la doble negación es equivalente a la ausencia de negación:

```python
not not True   # True
not not False  # False

print(not not is_even(10))  # => True
print(not not is_even(11))  # => False
```

Ahora sabes lo que significan los operadores **Y**, **O** y `not`. Con ellos, podrás crear condiciones compuestas a partir de dos o más expresiones lógicas.
