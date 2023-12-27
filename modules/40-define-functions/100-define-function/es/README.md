
Es más fácil escribir y mantener programas utilizando funciones propias. Permiten combinar operaciones compuestas en una sola. Por lo tanto, en esta lección hablaremos sobre cómo crear funciones propias.

Supongamos que queremos enviar correos electrónicos en un sitio web, esto es un proceso bastante complejo que implica interactuar con sistemas externos. Pero si definimos una función, toda la complejidad se ocultará detrás de una función simple:

```python
# Ejemplo hipotético
# Lugar donde se encuentra la función
from emails import send

email = 'support@hexlet.io'
title = 'Ayuda'
body = 'Escribí una historia de éxito, ¿cómo puedo obtener un descuento?'

# Una pequeña ejecución - mucha lógica interna
send(email, title, body)
```

Esta ejecución realiza acciones de gran lógica interna: se conecta al servidor de correo, forma una solicitud correcta basada en el título y el cuerpo del mensaje, y luego lo envía todo, sin olvidar cerrar la conexión.

Creemos nuestra primera función. Su tarea es mostrar un saludo en la pantalla:

```bash
Hello, Hexlet!
```

```python
# Definición de la función
# La definición no llama ni ejecuta la función
# Solo decimos que ahora existe esta función
def show_greeting():
    # Dentro del cuerpo, hay una sangría de cuatro espacios
    text = 'Hello, Hexlet!'
    print(text)

# Llamada a la función
show_greeting()  # => '¡Hola, Hexlet!'
```

https://replit.com/@hexlet/python-basics-define-function

A diferencia de los datos normales, las funciones realizan acciones. Por lo tanto, sus nombres deben indicarse con verbos: "construir algo", "dibujar algo", "abrir algo".

La descripción que se encuentra debajo del nombre de la función con sangría se llama **cuerpo de la función**. Dentro del cuerpo se puede describir cualquier código. Es como un pequeño programa independiente, un conjunto de instrucciones arbitrarias.

El cuerpo se ejecuta cuando se ejecuta la función. Cada llamada a la función ejecuta el cuerpo de forma independiente de otras llamadas.

El cuerpo de la función puede estar vacío, en ese caso se utiliza la palabra clave `pass`:

```python
# Definición mínima de una función
def noop():
    pass

noop()
```

El concepto de "crear una función" tiene muchos sinónimos: "implementar", "definir" e incluso "declarar". Se encuentran con frecuencia en la práctica. Al crear su propia función, facilitará las operaciones complejas y hará que el desarrollo sea más sencillo.
