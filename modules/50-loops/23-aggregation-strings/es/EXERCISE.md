
Implementa la función `sanitize_phone_number()`, que recibe un número de teléfono de un formulario y devuelve una cadena sin espacios, paréntesis ni guiones.

Los usuarios escriben los números de teléfono de distintas maneras, pero las aplicaciones suelen guardarlos en un solo formato. Recorre la cadena original carácter por carácter y construye un nuevo número solo con los caracteres útiles.

```python
sanitize_phone_number('+7 (999) 123-45-67')  # '+79991234567'
sanitize_phone_number('8 800 555 35 35')     # '88005553535'
sanitize_phone_number('(123) 456-7890')      # '1234567890'
```
