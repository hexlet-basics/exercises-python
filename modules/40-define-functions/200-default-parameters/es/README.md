Las funciones pueden recibir parámetros. A veces resulta cómodo fijar el valor directamente en la definición de la función, para no indicarlo en cada llamada. Ese valor se llama **valor por defecto**.

Si el argumento no se pasa, se usa ese valor. Si el argumento se indica, reemplaza el valor por defecto.

## Ejemplo: repetición de texto

Hagamos una función que repite una cadena varias veces. Por defecto, que sea una vez, pero si se quiere se puede indicar otra cantidad.

```python
def repeat(text, times=1):
    return text * times

print(repeat("Hi"))        # => Hi
print(repeat("Hi", 3))     # => HiHiHi
```

En este ejemplo se usa la operación de multiplicar una cadena por un número. Funciona así: se toma la cadena de partida y se repite la cantidad indicada de veces. Por ejemplo, `"A" * 5` se convertirá en `"AAAAA"`. Es una posibilidad incorporada de Python que se aplica a menudo al generar plantillas, separadores y fragmentos de texto repetidos.

```text
def repeat(text, times=2):    ← times tiene un valor por defecto
    ...

repeat('go')        →  times = 2  (por defecto)
repeat('go', 5)     →  times = 5  (indicado explícitamente)
```

Los parámetros opcionales se indican siempre al final de la lista de parámetros. Por eso en el ejemplo va primero el parámetro obligatorio `text` y solo después de él se sitúa el parámetro `times` con su valor por defecto.

## Ejemplo: unión de palabras con un separador

Por defecto las palabras se unen con un espacio, pero se puede indicar otro carácter.

```python
def join_words(word1, word2, sep=" "):
    return word1 + sep + word2

print(join_words("King", "Road"))          # => King Road
print(join_words("Dragon", "stone", "-"))  # => Dragon-stone
```

## Ejemplo: varios parámetros por defecto

Una función puede contener más de un parámetro con valores por defecto. Por ejemplo, hagamos una función que construye una cadena separadora. Por defecto el carácter es un guion y la longitud es 10.

```python
def make_line(symbol="-", length=10):
    return symbol * length

print(make_line())             # => ----------
print(make_line("*"))          # => **********
print(make_line("*", 5))       # => *****
print(make_line("#", 3))       # => ###
```
