Un mensaje puede contener los caracteres `<`, `>` y `&`. Al mostrarlo en una página HTML, el navegador puede interpretarlos como parte del marcado. El paquete `html` de la biblioteca estándar los sustituye por secuencias especiales para conservar el texto del mensaje.

## Tarea

Implementa la función `escape_html(text)`. Recibe una cadena y devuelve el resultado de `escape()` del paquete `html` con sus parámetros por defecto. También se sustituyen las comillas simples y dobles.

```python
print(escape_html("<b>A & B</b>"))  # => &lt;b&gt;A &amp; B&lt;/b&gt;
print(escape_html('"Hello"'))  # => &quot;Hello&quot;
print(escape_html("It's ok"))  # => It&#x27;s ok
print(escape_html("Hello"))  # => Hello
```

## Pistas

- `html` es un paquete regular de la biblioteca estándar. Su archivo _\_\_init\_\_.py_ proporciona la función `escape()`
- Puedes importar el paquete mediante `import html` o la función mediante `from html import escape`
- [Documentación de html.escape](https://docs.python.org/3/library/html.html#html.escape)
