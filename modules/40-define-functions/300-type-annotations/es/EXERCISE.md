La aplicación crea separadores de texto a partir de caracteres repetidos, por ejemplo `-------` o `=====`. Implementa la función `word_multiply()`. Debe recibir dos parámetros:

* Una cadena
* Un número que indica cuántas veces hay que repetir la cadena

Y devuelve la cadena repetida n veces. Si se pasa cero, se devuelve una cadena vacía.

```python
text = 'python'
print(word_multiply(text, 2)) # => pythonpython
print(word_multiply(text, 0)) # =>
```

Especifica las anotaciones de tipos al declarar la función.

## Pista

* No olvides que la anotación de tipo también hay que indicarla en el valor de retorno
