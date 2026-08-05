A menudo hay que construir cadenas a partir de varias partes, por ejemplo unir el nombre y el apellido, añadir una unidad de medida o componer un texto a partir de una plantilla. Para eso se usa la operación de concatenación, es decir, el pegado de cadenas.

## Cómo unir cadenas

En Python las cadenas se unen mediante el operador +. A pesar de que ese operador se usa también para sumar números, en el caso de las cadenas significa unión, es decir, pegar el contenido.

```python
print('Dragon' + 'stone')
# => Dragonstone
```

El orden importa. Primero va la parte izquierda ('Dragon'), después la derecha ('stone'). El resultado sale en el orden en que están indicados los operandos.

Así funciona la unión de varias cadenas. El código:

```python
print('Hello' + ', ' + 'World!')
```

La ejecución:

```text
'Hello' + ', ' + 'World!'
└──┬──┘   └┬┘   └──┬───┘
   └────┬───┘       │
  'Hello, '    +  'World!'
     └──────┬───────┘
      'Hello, World!'
```

Ejemplos.

```python
print('Kings' + 'wood')       # => Kingswood
print('Kings' + 'road')       # => Kingsroad
# Aquí por fuera hay comillas dobles, porque dentro hay una simple
print("King's" + 'Landing')   # => King'sLanding
```

Python permite unir cadenas incluso si están escritas con comillas distintas. Lo importante es que las dos partes sean cadenas.

## El espacio también es un carácter

Al unir, Python no inserta espacios automáticamente. Si entre las partes debe haber un espacio, hay que indicarlo a mano.

```python
# Espacio al final de la primera cadena
print("King's " + 'Landing')  # => King's Landing

# Espacio al principio de la segunda cadena
print("King's" + ' Landing')  # => King's Landing
```

El resultado será el mismo. Pero si no se añade el espacio, las palabras se pegarán.

## Secuencias de control

En las cadenas se pueden usar secuencias de control, por ejemplo `\n` para el salto de línea o `\t` para la tabulación. En la concatenación funcionan igual que cualquier otro carácter.

```python
print('Hello,' + '\n' + 'World!')
# =>
# Hello,
# World!

print('A' + '\t' + 'B')
# => A	B
```

## Conclusión

La concatenación es la unión de cadenas mediante `+`, y las cadenas se pueden unir independientemente del tipo de comillas.

- El pegado ocurre estrictamente en orden de izquierda a derecha.
- Los espacios no se añaden automáticamente, hay que incluirlos en las cadenas a mano.
