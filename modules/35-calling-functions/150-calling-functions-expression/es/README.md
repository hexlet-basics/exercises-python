Cuando escribimos programas, necesitamos enlazar las acciones unas con otras. La suma de números, la unión de cadenas y el trabajo con variables son ejemplos de cómo unos pasos simples se pueden combinar para obtener un comportamiento más complejo.

```python
rate = 10
hours = 5
salary = rate * hours + 100
print(salary)  # => 150
```

En programación, para eso se usa el concepto de **expresión**. Designa una construcción que se evalúa y da un resultado. En el ejemplo de arriba, `rate * hours + 100` es una expresión, compuesta de variables (`rate`, `hours`), un literal numérico (`100`) y operaciones aritméticas. Todo junto devuelve un resultado que se puede guardar en una variable o usar más adelante.

¿Qué nos aporta ese conocimiento? Entendemos que las expresiones se pueden combinar infinitamente, complicando la lógica poco a poco. Cada nueva expresión pasa a ser parte de una mayor:

```python
bonus = 50
# Expresión formada por muchas operaciones
salary = (rate * hours + bonus) * 12 - 500
print(salary)
```

Aquí varias expresiones se unieron en una y el resultado se volvió aún más complejo. Así es precisamente como se construyen los programas. Los pasos pequeños se suman en construcciones grandes. Por eso en programación es imposible aprender de memoria todas las combinaciones por adelantado. Es mucho más importante entender cómo se enlazan las expresiones entre sí hasta dar el resultado necesario.

## Las expresiones como argumentos de las funciones

El argumento de una función es siempre algún valor. Pero el valor no solo se puede escribir directamente, sino también calcular. Y eso significa que en los argumentos de una función se pueden sustituir cualesquiera expresiones.

```python
# Aquí el argumento de la función print es el número 150
print(150)

# Y aquí el argumento es una expresión, que primero se evalúa
print(10 * 15)  # => 150

# Se puede combinar de forma aún más compleja
rate = 10
hours = 15
bonus = 50
print(rate * hours + bonus)  # => 200
```

La función `print()` simplemente recibe un valor ya listo y lo muestra en pantalla. La forma de obtener ese valor le es indiferente a la función. Precisamente por eso las llamadas a funciones combinan perfectamente con cualquier expresión.

## Llamada a una función dentro de otra función

Como la llamada a una función es en sí misma una expresión, su resultado se puede pasar de inmediato a otra función. Eso permite construir construcciones aún más complejas.

```python
name = "python"

# La llamada len(name) devuelve 6
# Ese resultado se usa de inmediato como argumento de print()
print(len(name))  # => 6
```

Aquí `len(name)` se evalúa primero y devuelve el número 6. Después ese valor se sustituye en la llamada a `print()`. Esa combinación puede ser tan profunda como se quiera. El resultado de una función se puede pasar a otra y después a la siguiente.

Para leer correctamente esas construcciones hay que recordar el orden de las llamadas.

1. Primero se ejecuta la función que está "dentro", en nuestro caso `len(name)`.
2. Después su resultado se sustituye en el lugar de la llamada.
3. A continuación se ejecuta la función externa, en este caso `print()`.

Así pues, el código `print(len(name))` se puede descomponer mentalmente de esta forma:

```text
print(len('python'))

Paso 1:  len('python')  →  6
Paso 2:  print(6)       →  muestra 6
```

1. `len(name)` → `6`
2. `print(6)`
3. En la pantalla aparece `6`.

Ese principio funciona siempre. Primero se evalúan las llamadas anidadas y luego la externa.

## Uso de funciones como parte de expresiones

Las funciones devuelven valores, y eso significa que sus llamadas se pueden usar como argumentos de otras funciones y como parte de cualquier otra expresión.

```python
name = "python"

# La llamada len(name) devuelve 6
# Restamos 1 para obtener el índice del último carácter
last_index = len(name) - 1
print(last_index)  # => 5

# Se puede usar el resultado de la función en la aritmética
text = "hexlet"
double = len(text) * 2
print(double)  # => 12
```

Aquí las llamadas `len(name)` y `len(text)` son expresiones de pleno derecho. Devuelven valores que se pueden combinar con números, variables y otras operaciones.
