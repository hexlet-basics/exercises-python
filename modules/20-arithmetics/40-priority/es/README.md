Veamos una expresión simple:

```python
print(2 + 2 * 2)  # => 6
```

El resultado es 6, no 8. Esto se explica por el concepto de prioridad de las operaciones en matemáticas y en programación. Determina el orden en que se realizan las acciones:

- La multiplicación y la división se realizan antes que la suma y la resta.
- La potenciación (**) tiene una prioridad aún más alta.

```text
Prioridad de las operaciones (de alta a baja):

  **          potenciación
   ↓
  * / // %    multiplicación, división, resto
   ↓
  + -         suma, resta
```

Por ejemplo:

```python
print(2 * 2**3)  # => 16, porque primero 2 ** 3 = 8, después 8 * 2 = 16
```

Si van seguidas operaciones con la misma prioridad, se realizan de izquierda a derecha:

```python
print(8 / 2 * 3)  # => 12, porque primero 8 / 2 = 4, después 4 * 3 = 12
```

## Controlar el orden de las acciones

A veces hay que cambiar el orden de los cálculos. Para eso se usan los paréntesis. Permiten indicar qué acciones hay que realizar en primer lugar:

```python
print((2 + 2) * 2)  # => 8
```

Los paréntesis se pueden poner alrededor de cualquier parte de la expresión y anidarlos unos dentro de otros:

```python
print(3 ** (4 - 2))  # => 9
print(7 * 3 + (4 / 2) - (8 + (2 - 1)))  # => 14
```

La regla principal: cierra siempre los paréntesis. Los paréntesis sin pareja provocan errores: tanto los principiantes como los programadores con experiencia se olvidan a veces del paréntesis de cierre.

> Escribe los paréntesis de inmediato en pareja. Por ejemplo, teclea () y después rellena la parte de dentro. La mayoría de los editores de código (incluido el nuestro) añaden automáticamente el paréntesis de cierre en cuanto escribes el de apertura.

## Mejoramos la legibilidad

A veces una expresión funciona correctamente, pero se ve enredada. En esos casos los paréntesis se pueden añadir simplemente por claridad: no cambiarán el resultado, pero mejorarán la percepción.

```python
# Antes
print(8 / 2 + 5 - -3 / 2)  # => 10.5

# Después
print(((8 / 2) + 5) - (-3 / 2))  # => 10.5
```

Los programas los escriben personas, y también los leen personas. Al ordenador le da igual lo claro que esté escrito el código: basta con que sea sintácticamente correcto. Para una persona, un código claro y cuidado es garantía de comodidad, especialmente al trabajar en equipo o al analizar errores.
