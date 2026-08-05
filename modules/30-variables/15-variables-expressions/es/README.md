Ya sabemos que las expresiones se pueden componer de varias operaciones. Pero si se escribe todo el cálculo en una línea larga, el código se vuelve rápidamente difícil de leer.

Por ejemplo, esta forma de escribirlo funciona:

```python
yuans_count = 50 * 1.25 * 6.91
print(yuans_count)  # => 431.875
```

Python calculará esa expresión sin problema. Pero para una persona, leer ese código ya no resulta tan cómodo. Surgen preguntas de inmediato:

- ¿Qué significa `1.25`?
- ¿Qué significa `6.91`?
- ¿Dónde termina un paso del cálculo y empieza el siguiente?

Para hacer esos cálculos más claros, las variables se pueden usar dentro de otras expresiones. Primero el programa guarda el resultado intermedio en una variable, y después sustituye el valor de esa variable en el cálculo siguiente.

Las variables ayudan a dividir los cálculos complejos en partes comprensibles y a guardar los resultados intermedios.

## Conversión de divisas a través de una divisa intermedia

Imaginemos que hay que convertir euros a yuanes, pero que ese tipo de cambio directo no está disponible. Entonces lo haremos en dos pasos: **euros -> dólares -> yuanes**. Así funcionan a menudo los bancos al pagar compras en el extranjero.

## Paso 1. Euros -> Dólares

Supongamos el tipo de cambio: 1 euro = 1.25 dólares. Queremos convertir 50 euros:

```python
dollars_per_euro = 1.25
dollars_count = 50 * dollars_per_euro
print(dollars_count)  # => 62.5
```

En esa línea, `50 * dollars_per_euro` es una expresión, y `dollars_count` es la variable en la que se escribe el resultado. Python primero calcula la expresión y solo después guarda el resultado en la variable.

Al intérprete le da igual cómo esté escrita la expresión:

```python
dollars_count = 62.5
```

o

```python
dollars_count = 50 * dollars_per_euro
```

El resultado será el mismo. Pero para una persona la segunda variante es más útil: por el nombre `dollars_count` se ve de inmediato que en ese paso obtuvimos la cantidad en dólares.

## Paso 2. Dólares -> Yuanes

Ahora convertiremos 50 euros a yuanes usando el dólar como divisa intermedia. Supongamos los tipos de cambio: 1 dólar = 6.91 yuanes, 1 euro = 1.25 dólares.

```python
dollars_per_euro = 1.25
yuans_per_dollar = 6.91

dollars_count = 50 * dollars_per_euro
yuans_count = dollars_count * yuans_per_dollar

print(yuans_count)
```

Este código es más largo que la única línea `50 * 1.25 * 6.91`, pero leerlo es más fácil:

- se ve que `1.25` es el tipo de cambio del euro al dólar
- se ve que `6.91` es el tipo de cambio del dólar al yuan
- se ve que `dollars_count` es un resultado intermedio

Esto se notará especialmente si no vuelves al código durante al menos una semana. Y ahora imagina que en el proyecto hay cientos de miles de líneas de código. Si en esos proyectos no hubiera variables y cálculos intermedios, sería imposible entenderlos.

## Qué hay que recordar

- Si una expresión resulta demasiado larga, es mejor dividirla en varios pasos.
- Las variables ayudan a guardar los resultados intermedios y hacen los cálculos más claros.
- Cuando una variable se usa en una expresión, Python sustituye su valor y continúa el cálculo.
