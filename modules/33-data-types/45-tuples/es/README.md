Además de los primitivos, en Python hay tipos de datos compuestos, que guardan varios valores a la vez. Un estudiante de universidad se describe con el nombre, la edad y la nota media. Una película se describe con el título, el año de estreno y la valoración. Esos grupos de valores resulta cómodo guardarlos juntos, y no como un conjunto de variables separadas.

En Python hay incorporadas varias formas de trabajar con datos compuestos; la más simple de ellas es la tupla (tuple).

Imagina que queremos trabajar en el código con el concepto de estudiante, que tiene nombre, edad y nota media. Se puede intentar describir al estudiante con tres variables:

```python
student_name = 'Alice'
student_age = 20
student_score = 4.8
```

¿Y qué pasará si tenemos varios estudiantes? Saldrá un código muy torpe que nadie apreciará. Con las tuplas, en cambio, la vida se vuelve más interesante. Al estudiante se lo puede representar como una tupla.

Una tupla se escribe entre paréntesis, separando los valores con comas:

```python
student = ('Alice', 20, 4.8)       # nombre, edad, nota media

point = (10, 20)
film = ('Inception', 2010)    # título, año
user = ('Andrey Petrov', 'email@example.com', 'hexletcommunity', 100)    # nombre, email, telegram, edad
```

Los paréntesis se pueden omitir. Python determina la tupla por las comas.

```python
student = 'Alice', 20, 4.8       # nombre, edad, nota media

point = 10, 20
```

## Acceso a los elementos

Los elementos de una tupla se numeran desde cero. Se accede a ellos por índice, como en las cadenas.

```python
student = ('Alice', 20, 4.8)
print(student[0])  # => Alice
print(student[1])  # => 20
print(student[2])  # => 4.8
```

## Las tuplas son inmutables

Una vez creada, una tupla no se puede modificar. El intento de reemplazar un elemento provoca un error.

```python
student = ('Alice', 20, 4.8)
student[0] = 'Bob'  # TypeError: 'tuple' object does not support item assignment
```

Está hecho a propósito. La tupla se emplea donde un cambio accidental de los datos no es deseable: la configuración de conexión a una base de datos, el registro de un usuario, un catálogo con los días de la semana.

Si los datos hay que actualizarlos, se crea una tupla nueva y se reasigna la variable.

```python
student = ('Alice', 20, 4.8)
# usando los datos de la tupla anterior
student = (student[0], student[1] + 1, 4.9)  # pasó un año, la nota subió

print(student)  # => ('Alice', 21, 4.9)
```

La tupla antigua queda intacta (pero ya no se puede acceder a ella). La variable simplemente empieza a apuntar a la nueva.

## Desempaquetado

Los elementos de una tupla se pueden asignar a varias variables a la vez.

```python
student = ('Alice', 20, 4.8)
name, age, gpa = student

print(name)  # => Alice
print(age)   # => 20
print(gpa)   # => 4.8
```

Python empareja los valores con las variables por orden. La cantidad de variables debe coincidir con la cantidad de elementos.

## Aplicabilidad en la vida real

Las tuplas en Python aparecen con bastante frecuencia y se usan para guardar juntos varios valores relacionados. Normalmente se aplican en situaciones en las que el conjunto de datos tiene una estructura fija y no debe modificarse después de crearse. Por ejemplo, con una tupla se pueden guardar las coordenadas de un punto (10, 20) o un color (255, 0, 0). Las tuplas se consideran una de las estructuras de datos básicas del lenguaje y se usan con regularidad tanto en Python mismo como en muchas bibliotecas y frameworks.

Al mismo tiempo, para entidades más complejas, por ejemplo usuarios, pedidos o productos, las tuplas encajan mal, porque en ellas cuesta entender el sentido de cada valor, resulta incómodo guardar una gran cantidad de información y controlar los tipos de datos dentro de la estructura. Para esas tareas, en Python existen herramientas más adecuadas, que conoceremos en Hexlet.
