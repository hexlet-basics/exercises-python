En los programas reales surge a menudo la situación en la que hay que convertir datos de un tipo en otro. Es especialmente habitual, por ejemplo, al procesar la entrada del usuario o los datos de los formularios web. Ahí todo llega en forma de cadenas, incluso si introdujiste un número.

Para trabajar con esos valores hay que convertirlos explícitamente al tipo necesario, y para eso Python tiene su propio conjunto de funciones.

## Conversión de cadena a número

Imaginemos que recibimos del formulario la cadena '345' y necesitamos sumar ese número con otro:

```python
number = int("345")
print(number + 5)  # => 350
```

La función `int()` recibe una cadena y la convierte en un número entero.
Esa función se llama función de conversión de tipo (casting function).

```python
value = "0"
converted_value = int(value)
print(converted_value)  # => 0

print(int("10"))  # => 10
print(int(3.5))  # => 3  (la parte decimal se descarta)
```

```text
'123'  ──int()──→  123  ──float()──→  123.0
                    │
                 str()
                    ↓
                  '123'
```

## Conversión a cadena con str()

Si hace falta convertir un número o un valor lógico en cadena, usa la función `str()`:

```python
print(str(10))  # => '10'
print(str(True))  # => 'True'
print(str(3.5))  # => '3.5'
```

Esto es útil, por ejemplo, al formar textos, mensajes y salidas:

```python
age = 42
print("Age: " + str(age))  # => Age: 42
```

## Conversión a número de coma flotante con float()

Si hace falta un número con punto decimal, usa `float()`:

```python
print(float(5))  # => 5.0
print(float("2.7"))  # => 2.7
```
