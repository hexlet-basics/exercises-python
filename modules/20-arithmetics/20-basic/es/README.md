A nivel básico, las computadoras operan solo con números. Incluso en aplicaciones de alto nivel, hay muchos números y operaciones dentro de ellas. Pero para empezar, es suficiente conocer la aritmética básica, y eso es lo que haremos.

Por ejemplo, en matemáticas, escribimos la suma de dos números como: `3 + 4`. En programación, es lo mismo. Aquí hay un programa que suma dos números:

```python
3 + 4
```

La aritmética en programación es prácticamente igual a la aritmética escolar.

La línea de código `3 + 4` hace que el intérprete sume los números y obtenga el resultado. Este programa funcionará, pero no tiene sentido. Básicamente, no le estamos dando una instrucción al intérprete, simplemente le estamos diciendo: "mira, esta es la suma de tres y cuatro". En un trabajo real, no es suficiente informar al intérprete sobre una expresión matemática.

Por ejemplo, si estás creando una tienda en línea, no es suficiente pedirle al intérprete que calcule el costo de los productos en el carrito. Necesitas pedirle que calcule el costo **Y** mostrarle el precio al comprador.

Necesitamos pedirle al intérprete que sume `3 + 4` **Y** además darle una instrucción para hacer algo con el resultado. Por ejemplo, mostrarlo en la pantalla:

```python
# Primero se calcula la suma,
# luego, se pasa a la función de impresión
print(3 + 4)
```

Después de ejecutarlo, aparecerá el resultado en la pantalla:

```text
7
```

Además de la suma, están disponibles las siguientes operaciones:

* `-` — resta
* `*` — multiplicación
* `**` — exponente
* `/` — división
* `//` — [división entera](https://es.wikipedia.org/wiki/División_euclídea)
* `%` — [resto de la división](https://es.wikipedia.org/wiki/División_euclídea)

Ahora vamos a mostrar en pantalla el resultado de una división y luego el resultado de elevar un número a una potencia:

```python
print(8 / 2)   # => 4.0 (Al dividir dos números, el tipo de dato resultante es float)
print(3 ** 2)  # => 9
```


A veces, para mayor comodidad, mostraremos el resultado de ejecutar líneas de código de esta manera en los comentarios: `=> RESULTADO`. Por ejemplo, `# => 4`.

La primera instrucción mostrará `4` en la pantalla (porque 8 / 2 es igual a 4), y la segunda instrucción mostrará 9 en la pantalla (porque 3<sup>2</sup> es igual a 9).
