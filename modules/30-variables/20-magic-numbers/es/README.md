
Tomemos como ejemplo un programa que calcula el tipo de cambio de divisas:

```python
euros_count = 1000
dollars_count = euros_count * 1.25  # 1250.0
rubles_count = dollars_count * 60   # 75000.0

print(rubles_count)
```

Desde el punto de vista del desarrollo profesional, este código no cumple con las "mejores prácticas".

En este ejemplo, es difícil entender qué significan los números `60` y `1.25`. Imagina que tienes que trabajar con este código después de un mes o un año, será complicado. También será difícil para otros programadores que no hayan visto el código antes.

En nuestro ejemplo, es fácil deducir el contexto porque las variables están nombradas correctamente. Pero en proyectos reales, el código es mucho más complejo, por lo que a menudo es imposible adivinar el significado de los números.

El problema radica en los "números mágicos" — magic numbers. Estos son números cuyo origen no se puede entender a simple vista, es necesario profundizar en lo que sucede en el código.

Para evitar este problema, es necesario crear variables con nombres adecuados. Así todo encajará en su lugar:

 ```python
dollars_per_euro = 1.25
rubles_per_dollar = 60

euros_count = 1000
dollars_count = euros_count * dollars_per_euro     # 1250.0
rubles_count = dollars_count * rubles_per_dollar  # 75000.0

print(rubles_count)
```

En este programa:

* Se utiliza la convención de nombres snake_case
* Las dos nuevas variables se separan de los cálculos posteriores con una línea en blanco. Estas variables tienen sentido incluso sin los cálculos, por lo que esta separación es apropiada ya que mejora la legibilidad.
* El código resultante está bien nombrado y estructurado, pero es más largo que la versión anterior. Esto ocurre a menudo y es normal, ya que el código debe ser legible.

Los números mágicos y los nombres de variables confusos no rompen el código, pero lo hacen menos legible.

Es importante entender que la computadora ejecutará el cálculo especificado de todas formas. Sin embargo, otro programador que lea el código no entenderá nada, lo que dificultará el trabajo. Nombrar adecuadamente las variables es la mitad del éxito en el análisis del código.
