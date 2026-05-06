
Crea la función trim_and_repeat() con tres parámetros: una cadena de texto, offset (el número de caracteres a eliminar desde la izquierda) y repetitions (la cantidad de veces que se debe repetir la cadena recortada). Esta función recorta la cadena y repite la parte recortada tantas veces como sea necesario para alcanzar el número total de repeticiones especificado.
El valor predeterminado para offset es 0, y el valor predeterminado para repetitions es 1. La función debe combinar todas las repeticiones en una sola cadena y devolverla como resultado.

```python
text = 'python'
print(trim_and_repeat(text, offset=3, repetitions=2)) # => honhon
print(trim_and_repeat(text, repetitions=3)) # => pythonpythonpython
print(trim_and_repeat(text)) # => python
```
