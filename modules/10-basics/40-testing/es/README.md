
Nuestro sitio web verifica automáticamente tus soluciones (uso específico del término en programación). ¿Cómo funciona?

En los casos más simples, el sistema simplemente ejecuta tu código y verifica lo que se muestra en la pantalla. Luego lo compara con lo que "esperábamos" según la tarea.

En las lecciones más avanzadas, escribirás funciones, que son pequeños programas que toman información del mundo exterior y realizan operaciones con base en esta información. La verificación de tus soluciones en estos casos es un poco más complicada: el sistema ejecuta tu solución y le pasa cierta información. El sistema también sabe qué respuesta debería dar la función correcta con esos datos de entrada.

Por ejemplo, si tu tarea es escribir una función que sume dos números, el sistema de verificación le pasará diferentes combinaciones de números y comparará la respuesta de tu función con las sumas reales. Si las respuestas coinciden en todos los casos, se considera que la solución es correcta.

Este enfoque se llama pruebas y se utiliza en el desarrollo diario real. Por lo general, el programador primero escribe una prueba, que es un programa de verificación, y luego escribe el programa que quería escribir. Durante el proceso, ejecuta las pruebas constantemente y verifica si se acerca a la solución.

Es por eso que nuestro sitio web indica "Pruebas aprobadas" cuando resuelves correctamente un problema.

Aquí tienes un ejemplo sencillo: en una de las futuras lecciones, tendrás que escribir una función que realice cálculos y devuelva una respuesta. Supongamos que cometiste un pequeño error y la función devolvió un número incorrecto. El sistema responderá algo así:

```text
AssertionError: '10' != '35'
```

Lo más importante sigue después de los dos puntos: "el valor '10' no es igual al valor esperado '35'". Es decir, la función correcta debería haber devuelto 35, pero la solución actual no funciona correctamente y devuelve 10.

También vale la pena mencionar que si ves que en el editor ya hay algún código junto con los comentarios `BEGIN` y `END`, generalmente significa que debes escribir tu código entre estos comentarios. No debes modificar de antemano el código que se te proporciona, ya que esto puede afectar la verificación de la solución. En resumen, si ves líneas con los comentarios `BEGIN` y `END`, ¡escribe tu código en el espacio que se encuentra entre estos!

---

A veces, durante el proceso de resolución, puede parecer que has hecho todo correctamente, pero el sistema se comporta de manera "caprichosa" y no acepta la solución. Este comportamiento es prácticamente imposible. Las pruebas no funcionales simplemente no pueden llegar al sitio web; se ejecutan automáticamente después de cada cambio. En la gran mayoría de estos casos (y todos nuestros proyectos en conjunto han realizado millones de verificaciones a lo largo de los años), el error se encuentra en el código de la solución. Puede ser muy sutil, como haber ingresado accidentalmente una letra rusa en lugar de una letra en inglés; usar minúsculas en lugar de mayúsculas; o olvidar poner una coma, por ejemplo. Otros casos son más complicados. Es posible que tu solución funcione para un conjunto de datos de entrada, pero no funcione para otro. Por lo tanto, siempre lee atentamente la descripción del problema y los resultados de las pruebas. Casi seguro que habrá alguna indicación sobre el error.

Sin embargo, si estás seguro de que hay un error o has encontrado alguna imprecisión, siempre puedes señalarlo. Al final de cada teoría hay un enlace al contenido de la lección en GitHub (¡este proyecto es completamente abierto!). Al ir allí, puedes escribir un issue, ver el contenido de las pruebas (donde se muestra cómo se llama tu código) e incluso enviar un pull request. Si esto aún te resulta confuso, únete a nuestra [comunidad en Telegram](https://t.me/hexletcommunity/3), allí en el canal *'Feedback'* siempre estaremos dispuestos a ayudar.
