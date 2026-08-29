Mira la función de abajo. Determina el tipo de la oración por su último carácter: si la oración termina en un signo de interrogación, la función devolverá `Sentence is question`; en caso contrario, `Sentence is normal`:

```python
def get_type_of_sentence(sentence: str) -> str:
    last_char = sentence[-1]

    if last_char == "?":
        sentence_type = "question"
    else:
        sentence_type = "normal"

    return "Sentence is " + sentence_type


print(get_type_of_sentence("Hodor"))  # => Sentence is normal
print(get_type_of_sentence("Hodor?"))  # => Sentence is question
```

Añadimos `else` y un bloque nuevo. Se ejecutará si la condición del `if` resulta falsa. Además, dentro del bloque `else` se pueden anidar otras condiciones `if`. Else se traduce como "si no", "en otro caso".

```text
      ┌───────────┐
      │ ¿condición?│
      └─────┬─────┘
  True │           │ False
      ↓           ↓
┌──────────┐ ┌───────────┐
│ cuerpo if│ │cuerpo else│
└──────────┘ └───────────┘
```

Un ejemplo de bloques anidados:

```python
number = 10

if number > 10:
    print("Number is greater than 10")
else:
    if number == 10:
        print("Number is exactly 10")
    else:
        print("Number is less than 10")
```

La construcción `if-else` se puede escribir de dos formas. Con la negación se puede cambiar el orden de los bloques:

```python
def get_type_of_sentence(sentence: str) -> str:
    last_char = sentence[-1]

    if last_char != "?":
        sentence_type = "normal"
    else:
        sentence_type = "question"

    return "Sentence is " + sentence_type
```

Para que la construcción sea más fácil de escribir, procura elegir la comprobación sin negaciones y ajusta el contenido de los bloques a ella.

Con el ejemplo del uso de `else` se ve lo importante que es no olvidarse de separar los bloques.

```python
# Incorrecto
def check_number(number):
    if number > 0:
        print("El número es positivo")
    if number > 10:
        print("El número es mayor que 10")
    else:
        print("El número no es positivo")


check_number(3)
# => El número es positivo
# => El número no es positivo
```

En el ejemplo de arriba nos olvidamos de "anidar" con sangría el segundo `if`, por eso el `else` ahora se refiere al segundo `if`.

```python
# Correcto
def check_number(number: int) -> None:
    if number > 0:
        print("El número es positivo")
        if number > 10:
            print("El número es mayor que 10")
    else:
        print("El número no es positivo")


check_number(3)
# => El número es positivo
```

Ahora el segundo `if` está anidado en el primero, y el `else` está al mismo nivel que el primero y se opone a él.
