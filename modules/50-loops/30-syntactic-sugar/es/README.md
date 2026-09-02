En programación aparecen a menudo construcciones repetidas. En Python, como en muchos otros lenguajes, existe la posibilidad de acortar su escritura. Esas simplificaciones se llaman **azúcar sintáctico**. Hacen el proceso de escribir código más corto y más cómodo, conservando el mismo resultado.

## Formas abreviadas de asignación

A menudo hace falta modificar el valor de una variable, sumándole o restándole algo, multiplicándolo o dividiéndolo por un número. La variante básica se ve así:

```python
index = index + 1
count = count * 2
total = total - 5
price = price / 3
```

Python permite escribirlo de forma más corta, con los operadores combinados:

```python
index += 1  # lo mismo que index = index + 1
count *= 2  # lo mismo que count = count * 2
total -= 5  # lo mismo que total = total - 5
price /= 3  # lo mismo que price = price / 3
```

En los bucles esas abreviaturas aparecen con especial frecuencia. En ellos normalmente cambiamos el contador y acumulamos el resultado:

```python
sum = 0
index = 1

while index <= 5:
    sum += index  # lo mismo que sum = sum + index
    index += 1  # lo mismo que index = index + 1

print(sum)  # => 15
```

Sin las abreviaturas, el cuerpo del bucle sería más largo:

```python
while index <= 5:
    sum = sum + index
    index = index + 1
```

## Otras operaciones

Esa forma de escribir funciona con números y con otros tipos de datos.

Para las cadenas se usa el operador de concatenación:

```python
text = "Hello"
text += " World"  # lo mismo que text = text + " World"
```

## Abreviaturas admitidas

Existe una forma abreviada para casi todos los operadores: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`. Todas funcionan según el mismo principio: toman el valor actual de la variable, aplican la operación y guardan el resultado en la misma variable.
