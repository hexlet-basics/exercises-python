En Python, algunos tipos de datos se llaman **inmutables**. Eso significa que, una vez creados, su contenido no se puede modificar. A esos tipos primitivos pertenecen `int`, `float`, `str` y `bool`.

Veámoslo con el ejemplo de las cadenas.

### Los métodos de las cadenas no modifican el original

Cuando llamamos a un método de una cadena, parece que la estamos modificando. Por ejemplo, la pasamos a mayúsculas.

```python
text = "hexlet"
text.upper()
print(text)  # => hexlet
```

En realidad, el método `upper()` **devuelve una cadena nueva** en mayúsculas, y la cadena original `text` queda igual.

```text
text = 'Python'

text.upper()  →  'PYTHON'  (cadena nueva)
text          →  'Python'  (no cambió)
```

Para no perder el resultado, guardémoslo en una variable.

```python
text = "hexlet"
new_text = text.upper()
print(new_text)  # => HEXLET
```

Si no guardas el resultado del método en una variable nueva, simplemente lo perderás.

Los otros métodos funcionan igual.

```python
text = "   hi   "
cleaned = text.strip()
print(cleaned)  # => 'hi', el resultado no contiene espacios
print(text)  # => '   hi   ', la cadena no cambió, contiene espacios
```

El método `strip()` devolvió una cadena nueva sin espacios, pero el propio `text` no cambió.

Los métodos no modifican la cadena original porque las cadenas **no se pueden modificar después de crearse**. Esa decisión se tomó en Python a propósito. Modificar por accidente el valor de una cadena es imposible. Eso mismo simplifica el código **multihilo** y permite a Python reutilizar cadenas iguales en memoria, ahorrando recursos.

Más adelante verás que la mutabilidad y la inmutabilidad son propiedades importantes, sobre todo al pasar datos a las funciones y al trabajar con colecciones.

### Reasignación de la variable

El resultado del método se puede escribir de vuelta en la misma variable.

```python
text = "   hexlet   "
text = text.strip()
print(text)  # => 'hexlet'
```

Eso es apropiado cuando la esencia de los datos no cambia. Después de `strip()` es el mismo texto, solo más limpio. Si el resultado del método representa otra entidad, vale la pena darle un nombre aparte.

```python
full_name = "John Doe"
header_name = full_name.upper()
```

`full_name` es el nombre de la persona. `header_name` es su variante para el encabezado. Son cosas distintas, y guardarlas en una misma variable sería un lío. El nombre de la variable debe reflejar el sentido de los datos que guarda.
