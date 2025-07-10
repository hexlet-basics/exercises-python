
Los métodos son expresiones al igual que las variables o las llamadas a funciones, por lo tanto, se pueden combinar de diferentes maneras.

Por ejemplo, se pueden utilizar en operaciones:

```python
name = 'Shaya'
'hi, ' + name.upper() + '!'  # hi, SHAYA!
```

O se pueden utilizar como parámetros de funciones:

```python
name = 'robb'
print(name.lower())  # => robb
num1 = 5
num2 = 30
# bit_length() calcula la cantidad de bits necesarios para representar un número en binario
print(num1.bit_length() + num2.bit_length())  # => 8
```
