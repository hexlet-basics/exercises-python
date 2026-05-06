
Implementa la función `get_hidden_card()`, que recibe como entrada el número de una tarjeta de crédito (compuesto por 16 dígitos) como una cadena y devuelve su versión oculta, que se puede utilizar en el sitio web para su visualización. Si la tarjeta original tenía el número *2034399002125581*, entonces la versión oculta se verá así *\*\*\*\*5581*. En otras palabras, la función reemplaza los primeros 12 caracteres por asteriscos. El número de asteriscos se controla mediante el segundo parámetro, que es opcional. El valor predeterminado es 4.

```python
# La tarjeta de crédito se pasa como una cadena
# El segundo parámetro no se pasa, por lo que habrá 4 asteriscos
get_hidden_card('1234567812345678') # ****5678

get_hidden_card('1234567812345678', 2) # **5678
get_hidden_card('1234567812345678', 3) # ***5678

# O usando variables

card_number = '2034399002121100'
get_hidden_card(card_number) # ****1100
get_hidden_card(card_number, 1) # *1100
```

Para completar la tarea, necesitarás el mecanismo de repetición de cadenas, que repite una cadena un número determinado de veces. Para hacer esto, simplemente multiplica la cadena por el número de repeticiones:

```python
'+' * 5 # +++++
'o' * 3 # ooo
```
