Ya sabemos escribir funciones que comprueban condiciones sueltas. Y en esta lección aprenderemos a construir condiciones compuestas.

Supongamos que un sitio exige, al registrarse, que la contraseña tenga más de ocho caracteres y contenga al menos una letra mayúscula. Intentemos escribir dos expresiones lógicas separadas y unirlas con el operador especial "Y":

> La contraseña tiene más de 8 caracteres **Y** la contraseña contiene al menos una letra mayúscula

Esta es una función que recibe una contraseña y dice si cumple las condiciones (`True`) o no las cumple (`False`):

```python
def has_capital_letter(text: str) -> bool:
    # Comprueba la presencia de al menos una letra mayúscula en la cadena

def is_correct_password(password: str) -> bool:
   length = len(password)
   return length > 8 and has_capital_letter(password)

print(is_correct_password('Qwerty'))                   # => False
print(is_correct_password('Qwerty1234'))               # => True
print(is_correct_password('qwerty1234'))               # => False
```

El operador `and` significa "Y". En lógica matemática eso se llama conjunción. Toda la expresión se considera verdadera si es verdadero cada **operando**, es decir, cada una de las expresiones que la componen. En otras palabras, `and` significa "tanto una cosa como la otra". La prioridad de ese operador es menor que la de los operadores de comparación. Por eso la expresión `has_capital_letter(password) and length > 8` también funciona correctamente sin paréntesis.

Además de `and` se usa a menudo el operador `or`, que significa "O" (disyunción). Significa "o una cosa, o la otra, o las dos". La expresión `a or b` se considera verdadera si al menos uno de los operandos es verdadero o cuando los dos operandos son verdaderos. En el otro caso la expresión es falsa.

```python
def has_discount(age: int, is_student: bool) -> bool:
    return age < 18 or is_student


print(has_discount(15, False))  # => True  (menor de 18)
print(has_discount(25, True))  # => True  (estudiante)
print(has_discount(15, True))  # => True  (las dos condiciones)
print(has_discount(25, False))  # => False
```

Los operadores se pueden combinar en cualquier cantidad y en cualquier secuencia. Si en el código aparecen a la vez `and` y `or`, es mejor fijar la prioridad con paréntesis. Abajo hay un ejemplo de una función ampliada que determina la corrección de una contraseña:

```python
def has_capital_letter(text: str) -> bool:
    # Comprueba la presencia de al menos una letra mayúscula en la cadena
def has_special_chars(text: str) -> bool:
    # Comprueba la presencia de caracteres especiales en la cadena

def is_strong_password(password) -> bool:
    length = len(password)
    # Los paréntesis fijan la prioridad. Queda claro qué se refiere a qué.
    return (length > 8 and has_capital_letter(password)) and has_special_chars(password)
```

Ahora imaginemos que queremos comprar un piso que cumpla estas condiciones: una superficie de 100 metros cuadrados o más en cualquier calle **O** una superficie de 80 metros cuadrados o más, pero en la calle central `Main Street`.

Escribamos una función que compruebe el piso. Recibe dos argumentos: la superficie (un número) y el nombre de la calle (una cadena):

```python
def is_good_apartment(area: int, street: str) -> bool:
    return area >= 100 or (area >= 80 and street == "Main Street")


print(is_good_apartment(91, "Queens Street"))  # => False
print(is_good_apartment(78, "Queens Street"))  # => False
print(is_good_apartment(70, "Main Street"))  # => False

print(is_good_apartment(120, "Queens Street"))  # => True
print(is_good_apartment(120, "Main Street"))  # => True
print(is_good_apartment(80, "Main Street"))  # => True
```

El área de las matemáticas en la que se estudian los operadores lógicos se llama álgebra booleana. Las **tablas de verdad** muestran cuál será el resultado al aplicar cada operador.

#### Y `and`

| A     | B     | A and B  |
| ----- | ----- | -------- |
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
