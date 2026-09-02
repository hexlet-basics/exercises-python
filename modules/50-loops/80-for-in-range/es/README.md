Imagina que tenemos una serie de números del 0 al 9. Queremos sumar esos números. Podríamos hacerlo así:

```python
sum = 0
i = 0

while i < 10:
    sum += i
    i += 1

print(sum)  # => 45
```

Ese código lo podemos reescribir con el bucle `for` + `range()`

```python
sum = 0

for i in range(10):
    sum += i

print(sum)  # => 45
```

La función range en Python crea una secuencia de números dentro de un rango determinado. Se puede usar en el bucle for para controlar la cantidad de iteraciones.

Admite varias variantes de llamada. La forma `range(stop)` crea una secuencia desde 0 hasta `stop - 1`. La forma `range(start, stop)` crea una secuencia desde start hasta `stop - 1`. La forma `range(start, stop, step)` crea una secuencia de números desde start hasta `stop - 1` con el paso `step`.

De forma visual, las variantes de `range()` se ven así.

```text
range(1, 5)  →  1, 2, 3, 4
range(0, 3)  →  0, 1, 2
range(5)     →  0, 1, 2, 3, 4
                 └── empieza en 0, el final no se incluye
```

El ejemplo con un solo valor final lo vimos arriba. Veamos otro: imprimamos en pantalla los números del 1 al 3:

```python
for i in range(1, 4):
    print(i)

# => 1
# => 2
# => 3
```

Ahora intentemos mostrar los números en orden inverso

```python
for i in range(3, 0, -1):
    print(i)

# => 3
# => 2
# => 1
```

En los ejemplos de arriba vemos que la iteración termina antes del valor final.
