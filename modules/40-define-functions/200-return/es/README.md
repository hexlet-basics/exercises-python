
En esta lección vamos a profundizar en cómo trabajar con las funciones creadas para que sean útiles.

Cuando definimos una función, esta imprime algunos datos en la pantalla:

```python
def greeting():
    print('Hello, Hexlet!')
```

Estas funciones tienen poca utilidad, ya que no se puede utilizar su resultado dentro del programa. Veámoslo en un ejemplo.

Tomemos el caso de procesar un correo electrónico. Cuando un usuario se registra en un sitio web, puede ingresar su correo electrónico de diferentes maneras:

* Agregar espacios en blanco al principio o al final: `_support@hexlet.io__`
* Usar letras en diferentes casos: `SUPPORT@hexlet.io`

Si lo guardamos en la base de datos en ese formato, el usuario no podrá iniciar sesión en el sitio web. Para evitar esto, es necesario preparar el correo electrónico antes de guardarlo en la base de datos: convertirlo a minúsculas y eliminar los espacios en blanco alrededor del texto. Esta tarea se puede resolver en un par de líneas:

```python
def save_email():
    # El correo electrónico viene del formulario
    correo = '  SoPoRtE@hexlet.IO'
    # Eliminamos los espacios en blanco
    trimmed_email = email.strip()
    prepared_email = trimmed_email.lower()
    print(prepared_email)
    # Aquí se realizaría el guardado en la base de datos
```

Este código es posible gracias a que se devuelve un valor. Los métodos `strip()` y `lower()` no imprimen nada en la pantalla, sino que **devuelven** el resultado de su trabajo. Por eso podemos asignar ese resultado a variables. Si imprimieran en la pantalla, no podríamos asignar el resultado a una variable. Por ejemplo, no podemos hacer esto con la función `greeting()`:

```python
message = greeting()
# en realidad, la función print() devuelve None
# None es un objeto especial que se utiliza para representar la ausencia de valor
print(message) # => None
```

Ahora vamos a modificar la función `saludo()` para que devuelva datos. Para ello, en lugar de imprimir en la pantalla, utilizaremos la instrucción `return`:

```python
def greeting():
    return 'Hello, Hexlet!'
```

`return` es una instrucción que toma la expresión que se encuentra a su derecha y la devuelve al código que llamó al método. Aquí finaliza la ejecución de la función.

```python
# Ahora podemos utilizar el resultado de la función
message = greeting()
print(message) # => Hello, Hexlet!
# Incluso podemos realizar acciones con el resultado
print(mesagge.upper()) # => HELLO, HEXLET!
```

Cualquier código después de `return` no se ejecuta:

```python
def greeting_with_code_after_return():
    return 'Hello, Hexlet!'
    print('Nunca me ejecutaré')
```

Incluso si una función devuelve datos, eso no limita la posibilidad de imprimir en la pantalla. Además de devolver datos, también podemos imprimir:

```python
def greeting_with_return_and_printing():
    print('Apareceré en la consola')
    return 'Hello, Hexlet!'


# Esto imprimirá el texto en la pantalla y devolverá un valor
message = greeting_with_return_and_printing()
```

No solo se puede devolver un valor específico. Dado que `return` funciona con expresiones, puede haber cualquier cosa a la derecha de él. En este caso, debemos seguir los principios de legibilidad del código:

```python
def greeting():
    message = 'Hello, Hexlet!'
    return message
```

Aquí no estamos devolviendo la variable en sí, sino el valor que se encuentra en esa variable. A continuación, un ejemplo con cálculos:

```python
def double_five():
    # или return 5 + 5
    result = 5 + 5
    return result
```

No es suficiente con definir una función. También es importante que sea útil y que se pueda utilizar su resultado. Ahora, piensa qué devolverá la llamada a la función `run()` que se define a continuación.

```python
# Definición
def run():
    return 5
    return 10


# ¿Qué se imprimirá en la pantalla?
print(run())
```
