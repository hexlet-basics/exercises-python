
Construcciones como `index = index + 1` se utilizan frecuentemente en Python, por lo que los creadores del lenguaje agregaron una forma abreviada: `index += 1`.

Solamente difieren en la forma de escribirlos. El intérprete convertirá la construcción abreviada en la expandida.

Estas abreviaturas se llaman **azúcar sintáctico**, porque hacen que el proceso de escribir código sea un poco más fácil y agradable.

Esta forma aparece especialmente a menudo en los ciclos, donde normalmente cambiamos un contador y acumulamos un resultado:

```python
sum = 0
index = 1

while index <= 5:
    sum += index      # Lo mismo que sum = sum + index
    index += 1        # Lo mismo que index = index + 1

print(sum)  # => 15
```

Sin la forma abreviada, el cuerpo del ciclo sería más largo:

```python
while index <= 5:
    sum = sum + index
    index = index + 1
```

Existen formas abreviadas para todas las operaciones aritméticas y para la concatenación de cadenas:

* `a = a + 1` → `a += 1`
* `a = a - 1` → `a -= 1`
* `a = a * 2` → `a *= 2`
* `a = a / 1` → `a /= 1`
