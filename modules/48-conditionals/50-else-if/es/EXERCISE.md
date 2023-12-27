
En el mapa electrónico de Westeros implementado por Sam, los aliados de los Stark se representan con un círculo verde, los enemigos con un círculo rojo y las familias neutrales con un círculo gris.

Escribe una función para Sam llamada `who_is_this_house_to_starks()` que reciba el apellido de una familia y devuelva uno de los tres valores: `'friend'`, `'enemy'`, `'neutral'`.

Reglas de determinación:

  * Amigos (`'friend'`): `'Karstark'`, `'Tully'`
  * Enemigos (`'enemy'`): `'Lannister'`, `'Frey'`
  * Todas las demás familias se consideran neutrales (`'neutral'`)

Ejemplos de llamadas:

```python
print(who_is_this_house_to_starks('Karstark'))  # => 'friend'
print(who_is_this_house_to_starks('Frey'))      # => 'enemy'
print(who_is_this_house_to_starks('Joar'))      # => 'neutral'
print(who_is_this_house_to_starks('Ivanov'))    # => 'neutral'
```
