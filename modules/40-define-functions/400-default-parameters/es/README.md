
En programación, muchas funciones y métodos tienen parámetros que rara vez cambian. En estos casos, se les asignan valores predeterminados que se pueden cambiar según sea necesario. Esto reduce la cantidad de código repetitivo. Veamos cómo se ve esto en la práctica.

Veamos un ejemplo:

```python
# Función de potencia
# El segundo parámetro tiene un valor predeterminado de dos
def pow(x, base=2):
    return x ** base

# Tres al cuadrado (dos es el valor predeterminado)
pow(3)  # 3 * 3 = 9
# Tres al cubo
pow(3, 3)  # 3 * 3 * 3 = 27
```

https://replit.com/@hexlet/python-basics-define-functions-default-parameters

El valor predeterminado se ve como una asignación normal en la definición. Solo se activa si no se pasa el parámetro.

Imagina que no llevaste las piezas de repuesto para tu automóvil al taller. Entonces el mecánico te ofrecerá poner las que él tiene, por defecto.

Incluso puede haber un valor predeterminado cuando solo hay un parámetro:

```python
def my_print(text='nothing'):
    print(text)

my_print()  # => "nothing"
my_print("Hexlet")  # => "Hexlet"
```

Puede haber cualquier cantidad de parámetros con valores predeterminados:

```python
def f(a=5, b=10, c=100):
```

Los valores predeterminados tienen una restricción. Deben ir al final de la lista de parámetros. Desde el punto de vista de la sintaxis, no es posible crear una función en la que haya un parámetro opcional seguido de uno obligatorio:

```python
# Este código dará un error
def f(a=5, b=10, c=100, x):
# Y este también
def f(a=5, b=10, x, c=100):

# Este código funcionará
def f(x, a=5, b=10, c=100):

# Este también funcionará
def f(x, y, a=5, b=10, c=100):
```

Ahora sabes cómo trabajar con valores predeterminados de los parámetros. Pueden estar presentes en varios parámetros o en uno solo. Y recuerda que los valores predeterminados deben estar al final de la lista de parámetros. Este conocimiento te ayudará a reducir la cantidad de código repetitivo.
