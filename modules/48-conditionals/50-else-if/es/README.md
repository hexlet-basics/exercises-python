La función `get_type_of_sentence()` distingue solo las oraciones interrogativas y las normales. Añadámosle el soporte de las oraciones exclamativas:

```python
def get_type_of_sentence(sentence: str) -> str:
    last_char = sentence[-1]

    if last_char == "?":
        sentence_type = "question"

    if last_char == "!":
        sentence_type = "exclamation"
    else:
        sentence_type = "normal"

    return "Sentence is " + sentence_type


print(get_type_of_sentence("Who?"))  # => 'Sentence is normal'
print(get_type_of_sentence("No"))  # => 'Sentence is normal'
print(get_type_of_sentence("No!"))  # => 'Sentence is exclamation'
```

Añadimos la comprobación de las oraciones exclamativas. Técnicamente esa función funciona, pero interpreta mal las oraciones interrogativas. Además tiene problemas desde el punto de vista de la semántica. La presencia del signo de exclamación se comprueba en cualquier caso, incluso si ya se detectó un signo de interrogación. La rama `else` está descrita para la segunda condición, pero no para la primera. Por eso una oración interrogativa acaba siendo `"normal"`.

Para arreglar la situación, aprovechemos otra posibilidad de la construcción condicional:

```python
def get_type_of_sentence(sentence: str) -> str:
    last_char = sentence[-1]

    if last_char == "?":
        sentence_type = "question"
    elif last_char == "!":
        sentence_type = "exclamation"
    else:
        sentence_type = "normal"

    return "Sentence is " + sentence_type


print(get_type_of_sentence("Who?"))  # => 'Sentence is question'
print(get_type_of_sentence("No"))  # => 'Sentence is normal'
print(get_type_of_sentence("No!"))  # => 'Sentence is exclamation'
```

Ahora todas las condiciones se alinearon en una construcción única. La palabra clave `elif` significa "si no se cumplió la condición anterior, pero se cumple la actual".

```text
  ┌─────────────────┐
  │ ¿condición 1?   │
  └────┬────────┬───┘
  True │        │ False
        ↓        ↓
┌──────────┐  ┌─────────────────┐
│ cuerpo if│  │ ¿condición 2?   │
└──────────┘  └────┬────────┬───┘
              True │        │ False
                    ↓        ↓
          ┌───────────┐ ┌───────────┐
          │cuerpo elif│ │cuerpo else│
          └───────────┘ └───────────┘
```

La lógica de la función está montada así. Si la última letra es `?`, se devuelve `'question'`. Si la última letra es `!`, se devuelve `'exclamation'`. En todos los demás casos se devuelve `'normal'`.

Se ejecutará solo uno de los bloques de código que pertenecen a toda la construcción `if`.
