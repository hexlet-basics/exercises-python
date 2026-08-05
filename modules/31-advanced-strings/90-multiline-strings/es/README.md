A veces el texto de un programa tiene que estar formado por varias líneas. Por ejemplo, al generar un correo, al crear una plantilla, al formatear un mensaje de error o simplemente al trabajar con textos largos.

Por supuesto, se puede usar el carácter de salto de línea `\n`, como hacíamos antes:

```python
text = 'Un ejemplo de texto,\nformado por\nvarias líneas'
```

Al imprimirla, la cadena se verá así:

```text
Un ejemplo de texto,
formado por
varias líneas
```

Pero esa forma resulta incómoda, sobre todo si la cadena es larga o si hay que añadir saltos nuevos a menudo. Cada `\n` hay que insertarlo a mano, y eso empeora la legibilidad del código.

## Las cadenas multilínea (multi-line) como alternativa

En Python existe una forma más cómoda de escribir texto en varias líneas: las cadenas multilínea (multi-line strings). Para crear una cadena así hay que encerrar el texto entre comillas triples (técnicamente es una comilla repetida tres veces): `'''` o `"""`:

```python
text = '''Un ejemplo de texto,
formado por
varias líneas'''
```

Ahora en el código todo se ve igual que en la salida:

```text
Un ejemplo de texto,
formado por
varias líneas
```

## Cuidado con la línea vacía al final

Si cierras las comillas triples en una línea nueva, Python incluye también esa línea en el resultado:

```python
text = '''Un ejemplo de texto,
formado por
varias líneas
'''

print("====")
print(text)
print("====")
```

La salida:

```text
====
Un ejemplo de texto,
formado por
varias líneas

====
```

Fíjate: aparece una línea vacía al final. Para evitarla, no pases las comillas de cierre a una línea nueva:

```python
text = '''Un ejemplo de texto,
formado por
varias líneas'''
```

La salida:

```text
====
Un ejemplo de texto,
formado por
varias líneas
====
```

## Ventajas de las cadenas multi-line

- Legibilidad del código: el texto en el código se ve casi como en la pantalla.
- Comodidad al editar: es fácil añadir, borrar y cambiar líneas.
- No hace falta escapar las comillas:

```python
quote = '''Aquí no hay que escapar ni las comillas 'simples' ni las "dobles"'''
```

## Interpolación dentro de una cadena multilínea

Las cadenas multilínea se pueden combinar con las f-strings para sustituir valores de variables:

```python
a = 'A'
b = 'B'

text = f'''{a} y {b}
en líneas distintas'''
```

La salida:

```text
A y B
en líneas distintas
```

Esto resulta especialmente cómodo para plantillas, correos, mensajes de error y descripciones multilínea.

## El ordenador y la persona perciben el código de forma distinta

Python puede procesar tanto las cadenas con `\n` como las cadenas multilínea. Para el intérprete son lo mismo. Pero para la persona que lee el código, las cadenas multi-line son mucho más cómodas y claras.
