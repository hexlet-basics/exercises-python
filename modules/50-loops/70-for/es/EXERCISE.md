
En una de las lecciones anteriores, ya escribimos la función `filter_string()`. Recordemos que esta función recibe una cadena y un carácter, y devuelve una nueva cadena en la que se ha eliminado el carácter en todas sus posiciones. Esta vez, implementa esta función utilizando el ciclo `for`. Un requisito adicional es que el carácter a excluir no distingue entre mayúsculas y minúsculas.

Ejemplo de llamada:

```python
text = 'If I look forward I win'
filter_string(text, 'i')  # 'f  look forward  wn'
filter_string(text, 'O')  # 'If I lk frward I win'
```
