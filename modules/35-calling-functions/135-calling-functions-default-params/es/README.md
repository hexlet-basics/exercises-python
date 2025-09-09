
Veamos la función `round()`, que redondea un número que se le pasa como argumento:

```python
result = round(10.25, 0)  # 10.0
```

Le pasamos dos parámetros:

* El número que queremos redondear
* La precisión de redondeo

El valor `0` significa que se redondeará al número entero más cercano. En la mayoría de los casos, queremos redondear al número entero y no a los decimales. Por eso, los creadores de la función `round` hicieron el segundo parámetro **opcional** y le dieron un **valor por defecto de `0`**. Esto significa que podemos no especificar el segundo parámetro y el resultado será el mismo:

```python
result = round(10.25)  # 10.0
```

Y si queremos una precisión diferente, podemos pasar el parámetro:

```python
# redondeo a un decimal
result = round(10.25, 1)  # 10.2
```

Si una función en Python tiene argumentos opcionales, siempre se colocan después de los argumentos obligatorios. Pueden ser cualquier cantidad. Esto depende de la función en sí, pero siempre van juntos y al final de la lista de argumentos.
