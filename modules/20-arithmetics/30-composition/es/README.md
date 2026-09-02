En Python, igual que en matemáticas, se pueden combinar varias operaciones en una línea. El intérprete procesa esas expresiones paso a paso, según reglas determinadas.

Veamos un ejemplo:

```python
print(2 * 4 * 5 * 10)
```

Este código consta de varias operaciones de multiplicación combinadas en una sola expresión. Para entender cómo el intérprete ejecuta la expresión, la analizaremos por etapas:

- Primero se calcula `2 * 4`: `8 * 5 * 10`
- Después `8 * 5`: `40 * 10`
- Y por último `40 * 10`: `400`

El resultado final es `400`.

## ¿Y si las operaciones son distintas?

Todo es simple mientras se usan los mismos operadores. Pero ¿qué ocurrirá si se combinan, por ejemplo, la multiplicación y la suma?

```python
print(2 + 3 * 4)
```

```text
2 + 3 * 4
    └─┬─┘
2 +  12
└──┬───┘
   14
```

¿Saldrá `20` o `14`? La respuesta: `14`.

Esto se explica porque en Python, igual que en matemáticas, las operaciones tienen prioridad. La multiplicación se realiza antes que la suma si no se usan paréntesis. Lo veremos en detalle en la lección sobre prioridades.

## Ejemplos con la resta y con números negativos

La misma regla funciona para la resta:

```python
print(10 - 2 * 3)  # => 4
```

Primero se realiza la multiplicación: `10 - 6 = 4`.

Y si en la expresión hay números negativos, el menos unario se aplica después de la potenciación:

```python
print(-(2**2))  # => -4, dos elevado a dos, después se aplica el menos
print(-2 * 5)  # => -10, menos dos multiplicado por cinco
print(4 + -2)  # => 2
print(6 - -2)  # => 8
```

En todos los ejemplos, salvo el primero, primero se calcula el menos unario (`-2`) y después se realizan las demás operaciones.

Veamos con más detalle el último ejemplo:

```python
print(6 - -2)  # => 8
```

Primero se calcula el menos unario (`-2`), y entonces la operación se convierte en `6 - (-2)`, lo que da `8`. Es lo mismo que:

```python
print(6 + 2)  # => 8
```

## Qué hay que recordar

- Las expresiones pueden constar de varias operaciones.
- Python las calcula por etapas: de izquierda a derecha, respetando la prioridad de las operaciones.
- Los paréntesis se pueden usar para indicar de forma explícita el orden de los cálculos.
