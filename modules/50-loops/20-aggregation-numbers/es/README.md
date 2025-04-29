
Una clase de tareas que no se puede resolver sin bucles se llama **agregación de datos**. Estos problemas incluyen la búsqueda del valor máximo o mínimo, la suma y el promedio aritmético. En estos casos, el resultado depende de todo el conjunto de datos.

Para calcular la suma, es necesario sumar todos los números, y para calcular el máximo, es necesario compararlos. Los contadores o los especialistas en marketing están familiarizados con este tipo de problemas. Trabajan con tablas en Microsoft Excel o Google Sheets.

En esta lección, veremos cómo se aplica la agregación a los números y las cadenas de texto.

Supongamos que necesitamos encontrar la suma de un conjunto de números. Implementaremos una función que sume los números en un rango especificado, incluyendo los límites. Un **rango** es una serie de números desde un punto de inicio hasta un punto final específicos. Por ejemplo, el rango [1, 10] incluye todos los números enteros del uno al diez.

Ejemplo:

```python
sum_numbers_from_range(5, 7)  # 5 + 6 + 7 = 18
sum_numbers_from_range(1, 2)  # 1 + 2 = 3

# [1, 1] es un rango con el mismo inicio y fin, también es un rango
# Incluye un solo número, que es el límite del rango
sum_numbers_from_range(1, 1)      # 1
sum_numbers_from_range(100, 100)  # 100
```

Para implementar este código, necesitaremos un bucle, ya que la suma de números es un proceso iterativo, es decir, se repite para cada número. El número de iteraciones depende del tamaño del rango.

Echa un vistazo al siguiente código:

```python
def sum_numbers_from_range(start, finish):
    # Técnicamente, se puede cambiar el valor de inicio
    # Pero los argumentos de entrada deben mantenerse en su valor original
    # Esto hace que el código sea más fácil de analizar
    i = start
    sum = 0  # Inicialización de la suma
    while i <= end:  # Avanzamos hasta el final del rango
        suma = sum + i   # Calculamos la suma para cada número
        i = i + 1       # Pasamos al siguiente número en el rango
    # Devolvemos el resultado obtenido
    return sum
```


La estructura del bucle es estándar: hay un contador que se inicializa con el valor inicial del rango, un bucle con una condición de finalización cuando se alcanza el final del rango y una modificación del contador al final del cuerpo del bucle. El número de iteraciones en este tipo de bucle es igual a `fin - inicio + 1`. Para el rango [5, 7], esto es 7 - 5 + 1, es decir, tres iteraciones.

Las principales diferencias con el procesamiento normal son la lógica de cálculo del resultado. En los problemas de agregación, siempre hay una variable que almacena el resultado del bucle. En el código anterior, esta variable es `suma`. Se modifica en cada iteración del bucle, sumando el siguiente número del rango: `suma = suma + i`.

Este proceso se ve así:

```python
# para la llamada y ejecución sum_numbers_from_range(2, 5)
sum = 0
sum = sum + 2  # 2
sum = sum + 3  # 5
sum = sum + 4  # 9
sum = sum + 5  # 14
# 14 es el resultado de sumar los números en el rango [2, 5]
```

La variable `sum` tiene un valor inicial, desde el cual comienza cualquier operación repetitiva. En el ejemplo anterior, ese valor es `0`.

En matemáticas, hay un concepto de **elemento neutro** y cada operación tiene el suyo. La operación con este elemento no cambia el valor con el que se está trabajando. Por ejemplo, en la suma, cualquier número más cero es igual al número original. Lo mismo ocurre con la resta. La concatenación también tiene un elemento neutro, que es la cadena vacía: `'' + 'one'` será 'one'.
