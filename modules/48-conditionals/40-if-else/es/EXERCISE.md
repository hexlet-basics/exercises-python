Implementa la función `normalize_url()`, que realiza la normalización de los datos. Recibe la dirección de un sitio y la devuelve con `https://` al principio.

La función recibe direcciones en forma de `DIRECCIÓN` o `http://DIRECCIÓN`, pero siempre devuelve la dirección en forma de `https://DIRECCIÓN`. A la entrada de la función también puede llegar una dirección ya normalizada, `https://DIRECCIÓN`; en ese caso no hay que cambiar nada.

Ejemplos de llamadas:

```python
print(normalize_url("https://ya.ru"))  # => 'https://ya.ru'
print(normalize_url("google.com"))  # => 'https://google.com'
print(normalize_url("http://ai.fi"))  # => 'https://ai.fi'
```

Hay varias formas de resolver la tarea. Una de ellas es comparar los primeros 7 caracteres de la cadena-argumento con la cadena `http://` y luego, a partir de eso, añadirle o no `https://`.

También es probable que necesites descartar la parte innecesaria del principio de la cadena. ¿Recuerdas que vimos la forma de obtener un trozo de una cadena con un corte? Si no, te lo recuerdo:

```python
# Tomamos 2 caracteres desde el principio
print("python"[:2])  # => 'py'
```

Pues bien, con los cortes también se puede descartar una cantidad determinada de caracteres:

```python
# Descartamos los 2 primeros caracteres
print("python"[2:])  # => 'thon'
```
