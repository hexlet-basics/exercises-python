
En esta lección, vamos a analizar qué parámetros existen, cómo se diferencian y en qué casos se aplican.

**Argumentos** son los datos que se pasan a una función cuando se la llama. Hay dos tipos de argumentos:

El primer tipo son los **argumentos posicionales**. Se pasan en el mismo orden en el que se definen los parámetros de la función:

```python
# (text, length)
truncate('My Text', 3)
```

El segundo tipo son los **argumentos nombrados**. Se pasan no sólo como valores, sino como pares "nombre=valor". Por lo tanto, se pueden pasar en cualquier orden:

```python
# Los argumentos se pasan en un orden diferente
truncate(length=3, text='My Text')
```

Si observamos cuidadosamente los dos ejemplos anteriores, podemos entender que son dos funciones idénticas.

Ahora vamos a entender en qué casos se deben utilizar estos tipos de argumentos.

La elección del tipo de parámetro depende de quién llama a la función.

Hay dos razones para usar argumentos nombrados:

* Mejoran la legibilidad, ya que los nombres son visibles de inmediato.

* No es necesario especificar todos los parámetros intermedios que no necesitamos en este momento.

Esto último es útil cuando una función tiene muchos parámetros opcionales. Veamos un ejemplo:

```python
def print_params(a=1, b=2, c=3, d=4):
    print(a, b, c, d)

# Solo necesitamos pasar d, pero tenemos que pasar todos los demás
f(1, 2, 3, 8)

# Los argumentos nombrados nos permiten pasar solo d
# Los valores predeterminados se utilizan para los demás argumentos
f(d=8)
```

Los argumentos nombrados se pueden pasar junto con los posicionales. En ese caso, los posicionales deben ir al principio:

```python
# Pasamos solo a (posicional) y d (nombrado)
f(3, d=3)
```
