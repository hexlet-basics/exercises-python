Algunas funciones en Python tienen **parámetros opcionales**. Eso significa que para ellos hay fijado de antemano un valor por defecto, y al llamar a la función se puede no indicar ese parámetro.

![Taller mecánico](./assets/default-parameters.png)

Veamos la función incorporada `round()`, que redondea un número:

```python
result = round(10.25, 0)  # 10.0
```

Le pasamos dos valores:

- El número que hay que redondear.
- La precisión del redondeo; `0` significa que el redondeo será hasta el número entero.

Como lo que se necesita con más frecuencia es precisamente el redondeo al entero, los creadores de la función `round()` hicieron el segundo parámetro opcional y le pusieron el valor por defecto `0`. Por eso el resultado será el mismo incluso si no se indica el segundo parámetro:

```python
result = round(10.25)  # 10.0
```

Si hace falta otra precisión, se puede indicar explícitamente:

```python
# redondeo a un decimal
result = round(10.25, 1)  # 10.2
```

```text
round(10.25, 1)  →  argumentos: 10.25, 1   →  10.3
round(10.25)     →  argumentos: 10.25, (0)  →  10
                                       └── valor por defecto
```

La cantidad de parámetros opcionales depende de la función concreta, pero los obligatorios van siempre antes de los opcionales.

## La firma de la función

Cada función tiene una **firma**, que contiene la descripción de su nombre, sus parámetros y el orden en que se usan. La firma ayuda a entender qué datos espera la función y qué ocurrirá si no se indican los parámetros.

Miremos la [documentación](https://docs.python.org/3/library/functions.html#round) de la función `round()`.

```python
round(number, ndigits=None)
```

Esa es precisamente la firma. La función se llama `round`. El parámetro `number` es obligatorio: recibe el número a redondear. El parámetro `ndigits` tiene el valor por defecto `None`, es decir, es opcional; si no se indica, el redondeo se hará hasta el número entero.

## Cómo trabajar con funciones nuevas

Cuando te encuentras con una función nueva, puedes usar un patrón simple:

1. Abrir la documentación y encontrar la firma de la función.
2. Mirar los ejemplos de uso.
3. Pasar al intérprete interactivo de Python (REPL) e intentar llamar a la función con distintos argumentos.

Ese enfoque ayuda a entender rápido cómo funciona exactamente la función, cuáles son sus parámetros obligatorios y opcionales y qué resultados devuelve.
