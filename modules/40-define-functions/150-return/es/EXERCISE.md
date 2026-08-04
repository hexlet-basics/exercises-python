Completa la función `truncate()`, que recorta la cadena recibida a la cantidad indicada de caracteres, agrega puntos suspensivos al final y devuelve la cadena resultante. Esta lógica se usa a menudo en los sitios web para mostrar de forma abreviada un texto largo.

La función recibe dos parámetros:

1. La cadena que hay que recortar
2. La cantidad de caracteres que hay que dejar

Un ejemplo de cómo debe funcionar la función que escribas:

```python
# Pasamos el texto directamente
# Recortamos el texto dejando 2 caracteres
truncate('hexlet', 2)  # 'he...'

# A través de una variable
text = 'it works!'
# Recortamos el texto dejando 4 caracteres
truncate(text, 4)  # 'it w...'
```

La tarea se puede resolver de varias maneras; te sugerimos solo una de ellas. Para resolverla así necesitas tomar una subcadena de la cadena que se pasa como primer parámetro. Usa los cortes (slices) de cadenas. Según el enunciado, piensa desde qué índice y hasta cuál debes extraer la subcadena:

```python
word = 'welcome!'
index = 3
word[:index] # wel
```
