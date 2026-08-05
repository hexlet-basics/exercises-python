Nuestro sitio comprueba automáticamente tus soluciones. ¿Cómo funciona?

En el caso más simple, la comprobación ejecuta tu código y compara la salida en pantalla con el resultado esperado. Por ejemplo, si la tarea dice: «Muestra el número 10 en la pantalla», tu código en Python puede verse así:

```python
print(10)
```

La comprobación ejecutará ese código y verificará que en la pantalla apareció realmente `10`. Si la salida coincide con la esperada, la solución se acepta. Si no, verás un error:

```bash
E   AssertionError: assert '9' == '10'
E
E     - 10
E     + 9
```

La línea con `+` muestra el resultado real que devolvió tu código, y la línea con `-` el valor esperado.

En las lecciones siguientes, más complejas, escribirás funciones. Reciben datos y devuelven un resultado. En esas tareas la comprobación funciona un poco de otra manera: llama a tu función con distintos argumentos y sabe de antemano qué respuesta debe salir en cada caso.

Por ejemplo, si hay que escribir una función que sume dos números, la comprobación le pasará distintos pares de números y comparará el resultado con la suma correcta. Si en todos los casos las respuestas coinciden, la solución se considera correcta.

Ese enfoque se llama pruebas, y se usa en el desarrollo real. Las pruebas ayudan a comprobar si el programa funciona correctamente y a detectar rápido un error después de los cambios.

Precisamente por eso nuestro sitio dice «Pruebas aprobadas» cuando has resuelto bien la tarea.

## ¿Es mi error o no?

A veces, durante la resolución, parecerá que hiciste todo correctamente pero la comprobación no acepta la solución. Eso ocurre en muy raras ocasiones. Las pruebas se ejecutan automáticamente después de cada cambio, así que una comprobación rota normalmente no llega al sitio.

En la inmensa mayoría de esos casos el error está en el código de la solución. Puede ser muy poco visible: en lugar de una letra inglesa se escribió por accidente una rusa, en lugar de mayúscula se usó minúscula, o se olvidó mostrar una coma. También hay situaciones más complicadas. Por ejemplo, la solución funciona para un conjunto de datos de entrada, pero no para otro.

Por eso lee siempre con atención el enunciado de la tarea y la salida de las pruebas. Ahí casi con seguridad hay una indicación del error.

Y si estás seguro de que el problema está en la tarea o encontraste una imprecisión, escribe a nuestra [comunidad](https://t.me/hexletcommunity), al canal _'Feedback'_.
