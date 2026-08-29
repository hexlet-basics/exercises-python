En esta lección aprenderemos a escribir funciones que **devuelven valores**. Esas funciones responden a una pregunta y entregan el resultado de su trabajo, como si dijeran: "Toma, aquí lo tienes, ya lo he calculado".

Por ejemplo, una función puede devolver una cadena con el texto procesado o un número calculado con una fórmula. El valor devuelto se puede usar más adelante. Se guarda en una variable, se pasa a otra función o se muestra en pantalla.

Para que la función entregue el resultado, en ella se usa la palabra clave especial `return`. Termina la ejecución de la función e indica qué es exactamente lo que hay que devolver.

Este es un ejemplo de una función que pone el texto en mayúsculas:

```python
def shout(name):
    return name.upper()
```

Llamamos a `shout()`, le pasamos un nombre y obtenemos una cadena en mayúsculas. Esa cadena es el resultado de la función.

```python
result = shout("hexlet")
print(result)  # => HEXLET

result2 = shout("code-basics")
print(result2)  # => CODE-BASICS
```

A diferencia de `print()`, `return` no imprime nada. Simplemente devuelve el valor. La decisión de qué hacer con él la toma el código que llama.

Al llamar a la función `shout('hexlet')` se ejecuta primero la expresión `name.upper()`. Devuelve la cadena `'HEXLET'`. Después `return` entrega ese valor hacia fuera, allí desde donde se llamó a la función. En nuestro caso, ese valor se guarda en la variable `result` y luego se muestra en pantalla con `print()`.

## Devolución de una expresión evaluada

Las funciones no están obligadas a devolver simplemente un parámetro. Normalmente en `return` se indica una **expresión**, que primero se evalúa y luego su resultado se pasa hacia fuera.

```python
def full_name(first, last):
    return first.capitalize() + " " + last.capitalize()
```

En este ejemplo armamos el nombre completo a partir del nombre y el apellido. Primero se llama a los métodos `capitalize()`, luego las cadenas se unen con `+`, y la cadena ya lista se devuelve.

```python
name = full_name("Aria", "Stark")
print(name)  # => Aria Stark
```

Aquí, en la línea `return first.capitalize() + ' ' + last.capitalize()`, se ejecutan primero las dos llamadas a los métodos, luego se añade el espacio y solo entonces el resultado se pasa como valor de retorno.

## Funciones de varias líneas

A veces en el cuerpo de la función hay que dar varios pasos antes de obtener el resultado. En esos casos se escriben varias líneas de código y al final se usa `return` para devolver el valor final.

Por ejemplo, escribamos una función que formatea un nombre: elimina los espacios de los extremos y convierte todas las letras a mayúsculas.

```python
def format_name(name):
    clean = name.strip()
    uppercased = clean.upper()
    return uppercased
```

Primero quitamos los espacios con el método `strip()`, después pasamos a mayúsculas con `upper()` y devolvemos el valor final.

```python
print(format_name("  hexlet  "))  # => HEXLET
```

### Código después de `return`

Cuando Python llega al operador `return`, la ejecución de la función se detiene. Todo lo que esté escrito después de él dentro de la función **no se ejecutará**:

```python
def example():
    return "listo"
    print("este código nunca se ejecutará")
```

Por eso `return` se escribe siempre al final de la lógica. Sin embargo, esos finales dentro de una función pueden ser muchos. Lo veremos con más detalle cuando lleguemos a las expresiones condicionales.
