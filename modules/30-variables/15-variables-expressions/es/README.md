
Ya hemos aprendido cómo trabajar con variables para almacenar y reutilizar información. Pero también nos ayudan a simplificar cálculos complejos. Por ejemplo, convertir monedas o formar nuevas palabras. Veamos cómo hacerlo en la práctica.

Supongamos que necesitamos convertir euros a yuanes a través de dólares. Estas conversiones a través de una moneda intermedia son comunes en los bancos al realizar compras en el extranjero.

Primero, convirtamos 50 euros a dólares. Supongamos que un euro equivale a 1.25 dólares:

```python
dollars_count = 50 * 1.25
print(dollars_count)  # => 62.5
```

Aquí, en la variable `cantidad_dolares = 50 * 1.25`, a la derecha del signo igual, escribimos una **expresión**. El intérprete calculará el resultado (`62.5`) y lo asignará a la variable. Al intérprete no le importa cómo se escriben los datos: `62.5` o `50 * 1.25`. Ambas son expresiones que deben calcularse. Realiza los cálculos y llega al mismo valor: `62.5`.

Cualquier cadena de texto es una expresión. La concatenación de cadenas (unir los valores de las variables) también es una expresión. Cuando el intérprete encuentra una expresión, la procesa y genera un resultado: el **valor de la expresión**.

Aquí tienes algunos ejemplos de expresiones. A la derecha de cada expresión se muestran los valores resultantes:

```python
62.5             # 62.5
50 * 1.25        # 62.5
120 / 10 * 2     # 24.0
int('100')       # 100

'hello'          # hello
'Good' + 'will'  # Goodwill
```

En los lugares donde se espera una expresión, puedes colocar cualquier cálculo. No solo puede ser matemático, también puede ser una cadena de texto, como la concatenación. El programa seguirá funcionando correctamente.

Los programas están compuestos por muchas combinaciones de expresiones. Basándonos en lo que se ha dicho anteriormente, piensa si este código funcionará:

```python
who = "dragon's " + 'mother'
print(who)
```

Con variables, puedes realizar cálculos más complejos. Volvamos a nuestro programa de conversión de moneda. Guardemos el valor del dólar en yuanes como una variable separada. Calculemos el precio de 50 euros en dólares multiplicándolos por `1.25`. Supongamos que 1 dólar equivale a 6.91 yuanes:

```python
yuans_per_dollar = 6.91
dollars_count = 50 * 1.25  # 62.5
yuans_count = dollars_count * yuans_per_dollar  # 431.875

print(yuans_count)
```

Ahora agreguemos texto a la salida utilizando la concatenación:

```python
yuans_per_dollar = 6.91
dollars_count = 50 * 1.25  # 62.5
yuans_count = dollars_count * yuans_per_dollar  # 431.875

# La función str() convierte un número en una cadena de texto.
# Habrá una lección separada sobre estas conversiones.
print('The price is ' + str(yuans_count) + ' yuans')
# => The price is 431.875 yuans
```

Cualquier variable puede formar parte de cualquier expresión. En el momento de la evaluación, el valor de la variable se sustituye en lugar de su nombre.

El intérprete calcula el valor de `dollars_count` antes de que se utilice en otras expresiones. Cuando llega el momento de usar la variable, Python ya conoce su valor porque lo ha calculado.

Con variables, puedes realizar cálculos complejos y también generar una salida detallada con el valor resultante. Pero también puedes obtener nuevas expresiones al combinar dos o más valores de variables. Esto se logra mediante la concatenación.
