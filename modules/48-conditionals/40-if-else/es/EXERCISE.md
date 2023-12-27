
Implementa la función `normalize_url()`, que realiza la normalización de los datos. Recibe una dirección web y devuelve la misma con `https://` al principio.

La función acepta direcciones en forma de `DIRECCIÓN` o `http://DIRECCIÓN`, pero siempre devuelve la dirección en forma de `https://DIRECCIÓN`. También puede recibir una dirección ya normalizada `https://DIRECCIÓN`, en cuyo caso no se debe hacer ningún cambio.

Ejemplos de uso:

```python
print(normalize_url('https://ya.ru'))  # => 'https://ya.ru'
print(normalize_url('google.com'))     # => 'https://google.com'
print(normalize_url('http://ai.fi'))   # => 'https://ai.fi'
```

Hay varias formas de resolver este problema. Una de ellas es comparar los primeros 7 caracteres de la cadena de argumento con la cadena `http://` y luego agregar o no agregar `https://` en base a eso.

También es probable que necesites descartar la parte innecesaria al principio de la cadena. Recuerda que vimos cómo obtener una parte de una cadena usando el slicing. Si no lo recuerdas, aquí tienes un recordatorio:

```python
# Tomamos los primeros 6 caracteres
print('Invernalia'[:6])  # => 'Inver'
```

Así es, con el slicing también puedes descartar un número determinado de caracteres:

```python
# Descartamos los primeros 6 caracteres
print('Winterfell'[6:])  # => 'Winter'
```
