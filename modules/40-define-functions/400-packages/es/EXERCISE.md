Implementa la función `generate_pin()`. Devuelve un código PIN de cuatro dígitos aleatorio como cadena de texto.

Cada dígito del PIN es un entero aleatorio independiente del 0 al 9.

```python
print(generate_pin())  # => por ejemplo, "4823" o "0571"
print(generate_pin())  # => por ejemplo, "1942" o "0037"
```

Añade la anotación de tipo del valor de retorno.

## Pista

Genera cada uno de los cuatro dígitos con `random.randint(0, 9)` y combínalos en una cadena usando un f-string.
