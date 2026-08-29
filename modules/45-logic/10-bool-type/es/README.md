Además de las operaciones aritméticas, en matemáticas existen las operaciones de comparación, por ejemplo `5 > 4` o `3 < 1`. También existen en programación. Las comparaciones se aplican a menudo en tareas reales relacionadas con números. Por ejemplo, cuando tramitamos una compra en una tienda en línea, el sistema comprueba si al usuario le alcanza el dinero de la cuenta para pagar el producto. Si el importe de la cuenta es mayor o igual que el precio del producto, el pedido se confirma. Si faltan fondos, aparece el mensaje correspondiente.

## La comparación en programación

Empecemos con un ejemplo en el que se comparan dos números:

```python
print(5 > 4)  # => True
print(4 > 4)  # => False
```

El resultado de una comparación es un valor del tipo `bool`. Ese tipo tiene solo dos variantes posibles: `True` y `False`. Son valores especiales del lenguaje. Se pueden usar directamente:

```python
print(True)
print(False)
```

En la práctica rara vez se usan así, pero sobre ellos se construye la lógica del comportamiento del programa. Nos encontramos con eso literalmente todos los días, cuando introducimos códigos PIN y contraseñas, cuando ejecutamos acciones cuyo resultado puede tener distintas variantes. Todas esas variantes están escritas dentro del programa en forma de expresiones condicionales. El programa razona más o menos así: *si es de esta manera haz una cosa, si es de otra manera haz la otra*.

En Python están disponibles las siguientes operaciones de comparación:

* `<` y `<=` significan "menor" y "menor o igual"
* `>` y `>=` significan "mayor" y "mayor o igual"
* `==` y `!=` significan "igual" y "distinto"

Los lenguajes de programación adaptaron todas las operaciones matemáticas de comparación sin cambios, excepto los operadores de igualdad y desigualdad. En matemáticas para eso se usa el igual normal `=`, pero en programación el símbolo `=` se usa, la mayoría de las veces, para asignar valores a las variables. Por eso en Python se compara con `==`. Algunos ejemplos:

```python
print(5 >= 3)  # => True
print(7 < 0)  # => False
print(5 > 5)  # => False
print(5 >= 5)  # => True
print(2 == 5)  # => False
print(2 != 5)  # => True
```

Cuando en una comparación se usan valores concretos, esa operación parece carente de sentido: ya conocemos su resultado y siempre es el mismo, porque si 3 es mayor que 2, eso no cambia. Pero todo cambia cuando los valores pueden variar. Intentemos escribir una función simple que recibe la edad de un niño y determina si es un bebé. Se consideran bebés los niños de menos de dos años (el dos no se incluye).

```python
def is_infant(age: int) -> bool:
    return age < 2


print(is_infant(3))  # => False
print(is_infant(2))  # => False
print(is_infant(1))  # => True
print(is_infant(0))  # => True
```

Cuando las funciones devuelven el resultado de una comparación, normalmente responden a la pregunta con "sí" o "no". Esas funciones se llaman **predicados**. Se reconocen con facilidad porque devuelven un valor lógico `True` o `False`. A menudo en su nombre hay una pregunta o una afirmación que se puede comprobar ('is', 'has', 'can'). Esta es una función que comprueba si un número es negativo:

```python
def is_negative(number: int) -> bool:
    # Comprobamos si el número es menor que cero
    return number < 0


print(is_negative(-5))  # => True
print(is_negative(7))  # => False
```
