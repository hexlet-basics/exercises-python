Escribe la función `mask_card_number()`, que oculta el número de una tarjeta bancaria. La función debe reemplazar todos los caracteres de la cadena por `*`, excepto los cuatro últimos.

Los últimos cuatro caracteres empiezan en el índice `len(card_number) - 4`. Los caracteres con índices menores se reemplazan por `*`, y los demás se dejan como están.

Un ejemplo de funcionamiento:

```python
mask_card_number("1234567812345678")  # "************5678"
mask_card_number("12345678")  # "****5678"
```
