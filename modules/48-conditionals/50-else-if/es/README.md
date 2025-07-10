
La función `get_type_of_sentence()` solo distingue entre oraciones interrogativas y oraciones normales. Agregaremos soporte para oraciones exclamativas:

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'

    if last_char == '!':
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'

    return 'La oración es ' + sentence_type

print(get_type_of_sentence('¿Quién?'))  # => 'La oración es pregunta'
print(get_type_of_sentence('No'))    # => 'La oración es normal'
print(get_type_of_sentence('¡No!'))   # => 'La oración es exclamación'
```


Hemos agregado la verificación de oraciones exclamativas: 'exclamación'. Técnicamente, esta función funciona, pero interpreta incorrectamente las oraciones interrogativas. También tiene problemas desde el punto de vista semántico:

* Se verifica la presencia del signo de exclamación de todos modos, incluso si ya se ha detectado el signo de interrogación.
* La rama `else` está descrita para la segunda condición, pero no para la primera. Por lo tanto, la oración interrogativa se convierte en "normal".

Para corregir la situación, utilizaremos otra posibilidad de la construcción condicional:

```python
def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    elif last_char == '!':
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'

    return 'La oración es ' + sentence_type

print(get_type_of_sentence('¿Quién?'))  # => 'La oración es pregunta'
print(get_type_of_sentence('No'))    # => 'La oración es normal'
print(get_type_of_sentence('¡No!'))   # => 'La oración es exclamación'
```

Ahora todas las condiciones se han unificado en una sola construcción. `elif` significa "si la condición anterior no se cumple, pero la actual sí". La estructura resultante es la siguiente:

* si la última letra es `?`, entonces `'pregunta'`
* si la última letra es `!`, entonces `'exclamación'`
* para cualquier otro caso, `'normal'`

Solo se ejecutará uno de los bloques de código que pertenezca a toda la construcción `if`.
