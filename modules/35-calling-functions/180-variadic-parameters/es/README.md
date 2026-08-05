Algunas funciones tienen una particularidad: reciben un número variable de argumentos. No está relacionado con los valores por defecto, como en el caso de `round()`. Se trata de que la cantidad de datos que se pasan no está limitada a un número fijo.

Veamos la función `max()`. Encuentra el mayor valor entre los datos que se le pasan.

```python
print(max(1, 10, 3))       # => 10
print(max(1, -3, 2, 3, 2)) # => 3
```

En la documentación se pueden encontrar varias variantes de descripción de `max()`. Para simplificar la comprensión, nos centraremos en una, la que necesitamos ahora:

```python
max(arg1, arg2, /, *args, key=None)
```

Eso significa:

- la función exige como mínimo dos valores (`arg1` y `arg2`);
- después se pueden pasar tantos valores más como se quiera (`*args`);
- la función devolverá el mayor de los valores pasados.

Si entre los argumentos hay varios valores máximos iguales, se devuelve el primero de ellos.

```python
print(max(5, 5, 2))  # => 5
```

De forma análoga funciona la función `min()`, solo que busca el menor valor:

```python
print(min(1, 10, 3))       # => 1
print(min(1, -3, 2, 3, 2)) # => -3
```
