Al llamar a una función, los argumentos se pueden pasar de dos formas. En la **llamada posicional** los valores van estrictamente por orden. El primero cae en el primer parámetro y el segundo en el segundo. Los **argumentos con nombre** permiten indicar explícitamente en la llamada el nombre del parámetro. Eso resulta cómodo cuando la función tiene muchos parámetros y hay que redefinir solo algunos. Los demás se quedan con sus valores por defecto.

```python
def repeat(text, times=1):
    return text * times


repeat("Hi", 3)  # llamada posicional
repeat(text="Hi", times=3)  # llamada con nombres
```

Las dos variantes hacen lo mismo. En el segundo caso escribimos explícitamente que "Hi" es el valor de text y que 3 es el valor de times. Desde el punto de vista de la definición de la función nada cambió. Los argumentos con nombre funcionan para cualquier función, y la función misma no sabe nada de ello. Recibe los valores tal como están descritos en la definición.

```text
def truncate(text, length):
    ...

Posicionales:  truncate('hello', 3)
                        └──┬──┘  └┬┘
                        text    length

Con nombre:    truncate(length=3, text='hello')
                        └──┬───┘  └─────┬─────┘
                        length         text
```

Los argumentos con nombre se pueden indicar en cualquier orden. Eso no cambia el resultado del trabajo de la función, porque los valores se enlazan precisamente por el nombre del parámetro.

```python
repeat(times=3, text="Hi")  # => HiHiHi
```

Los argumentos con nombre se pueden combinar con los posicionales; en ese caso los posicionales van primero. Esa llamada permite indicar solo los parámetros que hay que redefinir.

```python
repeat("Hi", times=3)  # posicionales + con nombre => HiHiHi
```

## Cuándo usar los argumentos con nombre

Los argumentos con nombre son útiles cuando la función tiene varios parámetros y no hay que cambiarlos todos. En esos casos se pueden indicar solo los parámetros que importan en la llamada concreta y dejar los demás con sus valores por defecto.

```python
def make_line(symbol="-", length=10):
    return symbol * length


make_line()  # todos los parámetros por defecto

make_line(length=5)  # cambiamos solo la longitud
# Sin esto habría que escribirlo así
make_line("-", 5)
```

No hubo que indicar el carácter, incluso a pesar de que va antes que la longitud en la lista de parámetros. Los argumentos con nombre hacen las llamadas más claras. Al leer el código se ve de inmediato qué valor corresponde a qué parámetro.
