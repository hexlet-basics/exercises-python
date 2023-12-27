
Ya sabemos cómo escribir funciones que verifican condiciones individuales. En esta lección aprenderemos a construir condiciones compuestas.

Supongamos que un sitio web requiere que la contraseña tenga más de ocho caracteres y al menos una letra mayúscula al registrarse. Intentemos escribir dos expresiones lógicas separadas y combinarlas con el operador especial "Y":

> La contraseña tiene más de 8 caracteres **Y** la contraseña contiene al menos una letra mayúscula

Aquí hay una función que toma una contraseña y devuelve si cumple con las condiciones (`True`) o no (`False`):

```python
def has_capital_letter(string):
    # Verifica si hay al menos una letra mayúscula en la cadena

def is_correct_password(password):
   length = len(password)
   return length > 8 and has_capital_letter(password)

print(is_correct_password('Qwerty'))                   # => False
print(is_correct_password('Qwerty1234'))               # => True
print(is_correct_password('qwerty1234'))               # => False
```

`and` significa "Y". En lógica matemática, esto se llama conjunción. La expresión completa se considera verdadera si cada **operando** es verdadero, es decir, cada una de las expresiones compuestas. En otras palabras, `and` significa "y esto, y aquello". La prioridad de este operador es menor que la de los operadores de comparación. Por lo tanto, la expresión `has_capital_letter(password) and length > 8` también funciona correctamente sin paréntesis.

Además de `and`, se utiliza frecuentemente el operador `or` - "O" (disyunción). Significa "o esto, o aquello, o ambos". La expresión `a or b` se considera verdadera si al menos uno de los operandos o todos ellos son verdaderos. En caso contrario, la expresión es falsa.

Los operadores se pueden combinar en cualquier cantidad y en cualquier secuencia. Si en el código se encuentran `and` y `or` al mismo tiempo, se establece la prioridad mediante paréntesis. A continuación se muestra un ejemplo de una función extendida que determina la corrección de una contraseña:

```python
def has_capital_letter(string):
    # Verifica si hay al menos una letra mayúscula en la cadena

def has_special_chars(string):
    # Verifica si hay caracteres especiales en la cadena

def is_strong_password(password):
    length = len(password)
    # Los paréntesis establecen la prioridad. Es claro a qué se refiere cada uno.
    return (length > 8 and has_capital_letter(password)) and has_special_chars(password)
```

Ahora, imaginemos que queremos comprar un apartamento que cumpla con las siguientes condiciones: un área de al menos 100 metros cuadrados en cualquier calle **O** un área de al menos 80 metros cuadrados, pero en la calle principal `Main Street`.

Escribamos una función que verifique el apartamento. Toma dos argumentos: el área - un número y el nombre de la calle - una cadena:

```python
def is_good_apartment(area, street):
    return area >= 100 or (area >= 80 and street == 'Main Street')

print(is_good_apartment(91, 'Queens Street'))  # => False
print(is_good_apartment(78, 'Queens Street'))  # => False
print(is_good_apartment(70, 'Main Street'))    # => False

print(is_good_apartment(120, 'Queens Street'))  # => True
print(is_good_apartment(120, 'Main Street'))    # => True
print(is_good_apartment(80, 'Main Street'))     # => True
```

https://replit.com/@hexlet/python-basics-logic-logical-operators

El área de las matemáticas que estudia los operadores lógicos se llama álgebra booleana. A continuación, verás las **tablas de verdad** - con ellas puedes determinar el resultado al aplicar los operadores:

#### Y `and`

| A     | B     | A and B  |
| ----- | ----- | -------  |
| True  | True  | **True** |
| True  | False | False    |
| False | True  | False    |
| False | False | False    |

#### O `or`

| A     | B     | A or B   |
| ----- | ----- | -------- |
| True  | True  | **True** |
| True  | False | **True** |
| False | True  | **True** |
| False | False | False    |
