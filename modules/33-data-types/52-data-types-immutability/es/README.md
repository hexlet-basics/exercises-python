
Supongamos que queremos cambiar un carácter en una cadena de texto. Esto es lo que sucede:

```python
first_name = 'Alexander'
first_name[0] = 'B'
# Error: TypeError: 'str' object does not support item assignment
```

Esto ocurre debido a la inmutabilidad de los tipos primitivos en Python: el lenguaje no permite cambiar una cadena de texto físicamente. La inmutabilidad de los tipos primitivos es importante por varias razones. La razón principal es el rendimiento.

Pero a veces necesitamos cambiar una cadena de texto. Para eso existen las variables:

```python
first_name = 'Alexander'
first_name = 'Blexander'
print(first_name)  # => Blexander
```

Hay una gran diferencia entre *cambiar el valor de una variable* y *cambiar el valor en sí*. No se puede cambiar un tipo primitivo en Python, pero se puede cambiar un tipo compuesto. También se puede reemplazar el valor de una variable sin problemas.
