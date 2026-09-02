Antes ya pegábamos cadenas directamente usando la concatenación. Ahora haremos lo mismo, pero usando variables. La buena noticia: la sintaxis sigue siendo la misma. Simplemente se sustituyen los valores de las variables.

## Pegamos dos cadenas directamente

```python
what = "Kings" + "road"
print(what)  # => Kingsroad
```

Aquí todo es simple: dos cadenas se unen en una. Así funciona la concatenación: el operador + suma las cadenas creando una cadena nueva.

## Pegamos una cadena y una variable

Si en la variable first está la cadena "Kings", podemos pegarla tranquilamente con otra cadena:

```python
first = "Kings"
what = first + "road"
print(what)  # => Kingsroad
```

Python sustituirá el valor de la variable, realizará la operación y creará la cadena final.

## Pegamos dos variables

Exactamente igual se pueden unir los valores de dos variables, si las dos contienen cadenas:

```python
first = "Kings"
last = "road"
what = first + last
print(what)  # => Kingsroad
```

También se pueden añadir espacios:

```python
full = first + " " + last
print(full)  # => Kings road
```

```text
what = "Kings"
who  = 'road'

what    +  ' '  +  who
└─┬──┘           └──┬─┘
"Kings" + " "  + "road"
└────────┬─────────┘
    "Kings road"
```

## ¿Y qué pasa si la variable contiene un número?

Probemos así:

```python
age = 42
# print("Age: " + age)  #  ¡Error!
```

El programa dará un error: no se puede sumar una cadena y un número. Para pegar una cadena con un número hay que convertir el número en cadena:

```python
age = 42
print("Age: " + str(age))  #  Age: 42
```

Lo mismo ocurre con las variables que contienen resultados de cálculos:

```python
price = 50 * 1.25 * 6.91  # => 431.875
print("Price in yuans: " + str(price))  #  Price in yuans: 431.875
```

La función `str()` convierte cualquier valor (un número, el resultado de un cálculo, un booleano, etc.) en una cadena. De las funciones hablaremos en detalle en lecciones futuras.
