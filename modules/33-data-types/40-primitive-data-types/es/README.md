Los programas trabajan con información distinta: texto, números, fechas, listas, valores booleanos. Cada valor de un programa tiene un tipo.

Por ejemplo:

- "Hello, World!" es una cadena (`str`)
- 7, -198, 0 son números enteros (`int`)
- 3.14, -0.01, 1.0 son números racionales (`float`)

## ¿Qué es un tipo de dato?

Un tipo de dato determina:

- qué valores le corresponden;
- qué operaciones se pueden hacer con él.

Por ejemplo, los números se pueden sumar, dividir y multiplicar. Las cadenas, en cambio, se suman de otra manera: mediante la concatenación. Multiplicar una cadena por otra cadena no tiene sentido y no está permitido:

```python
# No se puede: 'mamá' * 'cuaderno'
```

## Los números y las cadenas son de tipos distintos

Un ejemplo de salida de un número:

```python
print(5)  # => 5
print(-5)  # => -5
```

Un ejemplo de salida de una cadena:

```python
print("5")  # => 5
print("-5")  # => -5
```

En la pantalla el resultado se ve igual, pero dentro del programa son cosas completamente distintas:

| Valor | Tipo de dato          |
| ----- | --------------------- |
| `5`   | `int` (número entero) |
| `'5'` | `str` (cadena)        |

La cadena '5' no se puede sumar con el número 5, igual que '10' / 2 no dará el número 5.0. Python protestará si intentas mezclar tipos incompatibles sin una conversión explícita.

## Números enteros y racionales

Python distingue dos clases de números:

- int denota los números enteros: -3, 0, 7, 100000
- float denota los números reales (racionales): 1.0, -3.14, 2.718

Un ejemplo:

```python
print(10.234)  # => 10.234
print(-0.4)  # => -0.4
```

En ellos se pueden escribir valores fraccionarios y usarlos en cálculos:

```python
print(3.5 + 1.2)  # => 4.7
print(5.0 / 2.0)  # => 2.5
print(2.75 - 0.5)  # => 2.25
```

## Tipos primitivos

Los tipos como:

- str (cadena),
- int (número entero),
- float (número racional)

se llaman primitivos: están incorporados directamente en el lenguaje.

```text
Tipos primitivos de Python
├── int    : números enteros      (7, -3, 0)
├── float  : números decimales    (3.14, -0.5)
├── str    : cadenas              ('hello')
└── bool   : tipo lógico          (True, False)
```

Además de las cadenas y los números, en Python hay un tipo booleano `bool` con los valores `True` y `False`, y también un valor especial, `None`. Con ellos nos encontraremos en detalle más adelante.

Existen también los tipos compuestos: listas, diccionarios, tuplas y otros. Los conoceremos más tarde. Más aún, en Python se pueden crear tipos propios (por ejemplo, clases), pero para empezar es importante entender bien los primitivos.
