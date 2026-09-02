Hasta este momento usábamos solo funciones ya listas: `print()`, `len()`, `max()` y otras. Pero en Python se pueden crear funciones propias, y llegó la hora de aprender a hacerlo.

## Para qué definir funciones

Supongamos que tenemos varios fragmentos de código parecidos:

```python
print("Hello, Hexlet!")
print("Hello, world!")
print("Hello, Python!")
```

Para no repetir la misma plantilla, podemos encapsularla en forma de función propia, que recibe un parámetro de entrada e imprime en pantalla la línea necesaria:

```python
def say_hello(name):
    print(f"Hello, {name}!")
```

Ahora podemos llamarla con distintos argumentos:

```python
say_hello("Hexlet")  # => Hello, Hexlet!
say_hello("world")  # => Hello, world!
say_hello("Python")  # => Hello, Python!
```

Al parecer la cantidad de código no disminuyó, pero apareció otra cosa. Si esa función se usa en distintos lugares, cuando haga falta cambiar el texto nos bastará con corregir solo la definición de la función. Y cuanto más compleja sea la tarea y más a menudo se use en distintos lugares, más importante es extraer la lógica a funciones propias.

## Sintaxis de la definición

```python
def nombre_de_la_función(parámetros):
    cuerpo
```

```text
def greet(name):              ← nombre de la función y parámetro
    return 'Hello, ' + name   ← cuerpo de la función
│         │
palabra   devolución
clave     del valor
```

La palabra clave `def` empieza la definición. En `nombre_de_la_función` se admite cualquier nombre, igual que en una variable; entre paréntesis se indica la lista de parámetros separados por comas. Después de los dos puntos se sitúa el cuerpo de la función con una sangría de 4 espacios, en el que se escribe código Python normal.

En Python las sangrías tienen valor sintáctico. Muestran qué código pertenece al cuerpo de la función. Mira el ejemplo:

```python
def say_hi():
    print("Hi!")


print("El programa continúa…")
```

Aquí la función `say_hi()` está definida, pero **`print('El programa continúa…')`** no pertenece a la función, porque no tiene sangría. Se ejecutará de inmediato al arrancar el programa, independientemente de la llamada a `say_hi()`.

Para que `say_hi()` actúe, hay que llamarla explícitamente:

```python
def say_hi():
    print("Hi!")


say_hi()  # => Hi!
print("El programa continúa…")
```

## Ejemplo: función para imprimir la media aritmética

Ahora implementaremos una función simple que **calcula e imprime la media aritmética** de dos números. La media aritmética es la suma de los números dividida entre su cantidad. Por ejemplo, la media de 6 y 4 se calcula así: `(6 + 4) / 2 = 5`.

```python
def print_average(a, b):
    total = a + b
    average = total / 2
    print(average)


print_average(6, 4)  # => 5.0
```

Aquí `a` y `b` son los parámetros de entrada, `total` contiene su suma, `average` se obtiene dividiendo la suma entre 2 y `print()` muestra el resultado.

Al llamar a `print_average(6, 4)`, en la pantalla se mostrará `5.0`.

## Reutilización y legibilidad

Las funciones ayudan a evitar la duplicación y hacen que los programas sean más comprensibles. El nombre de la función por sí solo dice qué hace. Eso es especialmente importante en proyectos grandes, donde el código lo leen otros programadores (o tú mismo un mes después).
