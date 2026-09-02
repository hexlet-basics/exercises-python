Además del propio código, en los archivos fuente se encuentran a menudo comentarios. Son líneas que el intérprete no procesa. Los programadores las escriben para explicar cómo funciona el código, señalar errores o recordar qué queda por terminar.

```python
# Eliminar la línea de abajo después de implementar la tarea de registro
print(10)
```

En Python todos los comentarios son de una sola línea. Empiezan con el símbolo especial #, tras el cual puede ir cualquier texto. Todo lo escrito después de # lo ignora el intérprete.

```text
# comentario     ──→  [ omitido por el intérprete ]
print('hello')  ──→  [ ejecutado → hello ]
# otro más       ──→  [ omitido por el intérprete ]
```

Un comentario puede ocupar toda la línea:

```python
# For Winterfell!
# For Lanisters!
```

O estar al final de una línea con código:

```python
print("I am the King")  # For Lannisters!
```

Si hace falta dejar una explicación larga, se usan varias líneas con #:

```python
# The night is dark and
# full of terrors.
print("I am the King")
```

El intérprete ignora los comentarios. Los desarrolladores, gracias a ellos, entienden más rápido el código ajeno y no olvidan detalles importantes en el propio.

## Comentarios de servicio

Durante el trabajo te encontrarás con este código en nuestro editor:

```python
# BEGIN

# END
```

_BEGIN_ y _END_ aquí son comentarios normales que no influyen de ninguna manera en el funcionamiento del programa. Muestran dónde escribir el código de la tarea.

```python
# BEGIN
<aquí tu solución>
# END
```

Cuando veas _BEGIN_ y _END_, escribe tu código entre ellos y deja el resto sin cambios.
