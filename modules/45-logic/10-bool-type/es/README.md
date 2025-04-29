
Además de las operaciones aritméticas en matemáticas, existen operaciones de comparación, como `5 > 4` o `3 < 1`. También existen en programación. Por ejemplo, cuando ingresamos a un sitio web, se comparan el nombre de usuario y la contraseña ingresados con los que están en la base de datos. Si coinciden, se nos permite ingresar, es decir, se autentica. En esta lección, aprenderemos sobre las operaciones de comparación.

Los lenguajes de programación han adaptado todas las operaciones de comparación matemáticas sin cambios, excepto los operadores de igualdad y desigualdad. En matemáticas, se utiliza el signo de igual `=`, pero en programación esto rara vez se encuentra.

En muchos lenguajes, el símbolo `=` se utiliza para asignar valores a variables. Por lo tanto, en Python se compara con `==`.

Lista de operaciones de comparación:

* `<`  — menor que
* `<=` — menor o igual que
* `>`  — mayor que
* `>=` — mayor o igual que
* `==` — igual que
* `!=` — no igual que

Estas operaciones no solo se aplican a números. Por ejemplo, con el operador de igualdad se pueden comparar cadenas de texto: `password == text` es una comparación de identidad entre cadenas de texto que están almacenadas en diferentes variables.

Una operación lógica como `5 > 4` o `password == text` es una expresión. Su resultado es un valor especial, `True` (verdadero) o `False` (falso). Este es un nuevo tipo de dato para nosotros, el tipo `bool`.

```python
result = 5 > 4
print(result)  # => True
print('one' != 'one')  # => False
```

Junto con las cadenas de texto (`str`) y los números enteros y racionales, el **tipo `bool` (booleano)** es uno de los tipos de datos primitivos en Python.

Intentemos escribir una función simple que tome la edad de un niño y determine si es un bebé. Se considera bebé a los niños menores de un año:

```python
def is_infant(age):
    return age < 1

print(is_infant(3))  # => False
```


Cualquier operación es una expresión, por lo que en una sola línea de la función escribimos "devolver el valor que resulte de la comparación `age < 1`". Dependiendo del argumento que se pase, la comparación será verdadera (`True`) o falsa (`False`), y `return` devolverá ese resultado.

Ahora probemos con un niño de seis meses:

```python
print(is_infant(0.5))  # => True
```

El resultado de la operación es `True`. Por lo tanto, el niño es realmente un bebé.
