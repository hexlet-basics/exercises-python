
Completa la función `truncate()`, que recorta una cadena pasada como parámetro hasta un número determinado de caracteres, agrega puntos suspensivos al final y devuelve la cadena resultante. Esta lógica se utiliza a menudo en sitios web para mostrar texto largo de forma abreviada.

La función recibe dos parámetros:

1. La cadena que se debe recortar
2. El número de caracteres que se deben mantener

Aquí tienes un ejemplo de cómo debería funcionar la función que escribas:

```python
# Pasando el texto directamente
# Recortamos el texto dejando 2 caracteres
recortar('hexlet', 2)  # 'he...'

# A través de una variable
text = 'it works!!'
# Recortamos el texto dejando 4 caracteres
truncate(text, 4)  # '¡it w...'
```

Puedes resolver este ejercicio de diferentes maneras, pero te daremos una pista. Para resolverlo de esta manera, tendrás que tomar una subcadena de la cadena que se pasa como primer parámetro a la función. Utiliza segmentos de cadenas para hacerlo. Piensa, en función del enunciado, desde qué índice y hasta qué índice debes extraer la subcadena.

```python
word = 'welcome!'
index = 3
word[:index] # wel
```
