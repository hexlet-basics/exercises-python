
Las funciones no solamente pueden devolver valores, sino también recibir parámetros. En esta lección aprenderemos a crear funciones que acepten parámetros.

Recordemos que ya nos hemos encontrado con funciones que tienen parámetros:

```python
# Recibe un parámetro de cualquier tipo
print('soy un parámetro')
# Recibe dos parámetros de tipo cadena
# el primero es lo que buscamos, el segundo es por qué lo reemplazamos
'google'.replace('go', 'mo')  # moogle
# Recibe dos parámetros numéricos
# el primero es el número a redondear, el segundo es la cantidad de decimales que queremos mantener
round(10.23456, 3)  # 10.235
```

Ahora imaginemos que necesitamos implementar la función `get_last_char()`, que devuelve el último carácter de una cadena que se le pasa como parámetro.

Así es como se usaría esta función:

```python
# Pasando los parámetros directamente sin variables
get_last_char("Hexlet")  # t
# Pasando los parámetros a través de variables
name1 = 'Hexlet'
get_last_char(name1)  # t
name2 = 'Goo'
get_last_char(name2)  # o
```

De este ejemplo podemos sacar las siguientes conclusiones:

* Necesitamos definir la función `get_last_char()`
* La función debe recibir un parámetro de tipo cadena
* La función debe devolver un valor de tipo cadena

Definimos la función:

```python
def get_last_char(text):
    return text[-1]
```

Entre paréntesis se especifica el nombre de la variable `text`, que es el parámetro. El nombre del parámetro puede ser cualquier cosa, lo importante es que refleje el significado del valor que contiene. Por ejemplo:

```python
def get_last_char(string):
    return string[-1]
```

El valor del parámetro dependerá de cómo se llame a esta función:

```python
# Dentro de la función, string será igual a 'hexlet'
get_last_char('hexlet')  # t

# Dentro de la función, string será igual a 'code'
get_last_char('code')  # e

# Dentro de la función, cadena o string será igual a 'Winter is coming'
# El nombre de la variable fuera de la función no está relacionado con el nombre de la variable en la definición de la función
text = 'Winter is coming'
get_last_char(text)  # g
```

https://replit.com/@hexlet/python-basics-define-functions-parameters

Es obligatorio especificar el parámetro. Si se llama a la función sin él, el intérprete mostrará un error:

```python
get_last_char()  # Este código no tiene sentido

TypeError: get_last_char() missing 1 required positional argument: 'string'
```

Muchas funciones trabajan con varios parámetros al mismo tiempo. Por ejemplo, para redondear números, es necesario especificar tanto el número en sí como la cantidad de decimales:

```python
round(10.23456, 3)  # 10.235
```

Lo mismo ocurre con los métodos. Pueden requerir cualquier cantidad de parámetros para funcionar:

```python
# El primer parámetro es lo que buscamos
# El segundo parámetro es por qué lo reemplazamos
'google'.replace('go', 'mo')  # moogle
```

Para crear funciones y métodos de este tipo, es necesario especificar la cantidad necesaria de parámetros separados por comas. También es importante darles nombres descriptivos.

A continuación se muestra un ejemplo de definición de la función `replace()`, que reemplaza una parte de una cadena por otra:

```python
def replace(text, from, to):
    # Aquí va el cuerpo de la función
    # pero lo omitimos para no distraernos

replace('google', 'go', 'mo')  # moogle
```

Cuando hay dos o más parámetros, el orden en que se pasan a la función es casi siempre importante. Si se cambia el orden, la función se comportará de manera diferente:

```python
# No se reemplaza nada,
# ya que no hay 'mo' en 'google'
replace('google', 'mo', 'go')  # google
```

Ahora sabes cómo crear funciones que pueden recibir parámetros.
