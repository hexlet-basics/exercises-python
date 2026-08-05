`greeting` sirve de ejemplo de un nombre de variable simple y claro. Pero a menudo nombres como `name`, `email` o `price` resultan insuficientes. Por ejemplo, hay que describir el nombre del usuario, la cantidad total de pedidos, la longitud máxima de un mensaje. Esos nombres ya constan de varias palabras. ¿Cómo se verá en ese caso el nombre de la variable?

En los distintos lenguajes de programación se usan estilos de nomenclatura distintos. De eso depende cómo se verá un nombre de variable de varias palabras. Por ejemplo, así se puede escribir una variable que guarda la longitud máxima de un mensaje:

1. `maxmessagelength`
1. `maxMessageLength`
1. `max-message-length`
1. `max_message_length`

## Los estilos principales

Estos son tres enfoques populares para escribir nombres compuestos:

- kebab-case: las palabras se separan con guion: `max-message-length`.

  En Python no funciona, ya que el guion (-) se percibe como el operador de resta.

- snake_case: las palabras se separan con subrayado: `max_message_length`.

  Es el estándar para Python.

- CamelCase (o UpperCamelCase): cada palabra con letra mayúscula, sin separadores: `maxMessageLength`.

## Cómo se hace correctamente en Python

```python
user_name = "Daenerys"
max_length = 280
total_orders_count = 17
```

- Todas las letras en minúscula
- Las palabras se separan con el carácter de subrayado

## Cómo no hay que hacerlo

No conviene incluir el tipo de dato en el nombre de la variable. Esos nombres se leen peor y quedan obsoletos rápido. Por ejemplo, `user_name_string` o `messages_number` describen no el sentido de la variable, sino su implementación técnica.

El nombre debe responder a la pregunta «¿qué se guarda?», no «¿de qué tipo es?». Por eso es mejor escribir `user_name` en lugar de `user_name_string`, y `messages_count` en lugar de `messages_number`.
