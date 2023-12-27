
Los sitios web envían constantemente correos electrónicos a sus usuarios. Una tarea típica es enviar automáticamente un correo electrónico personalizado, donde el nombre del usuario estará en el encabezado. Si el nombre de la persona se almacena en algún lugar de la base de datos del sitio como una cadena, la tarea de generar el encabezado se reduce a la concatenación: por ejemplo, es necesario unir la cadena `Hola` con la cadena que contiene el nombre.

Escriba un programa que genere el encabezado y el cuerpo del correo electrónico, utilizando variables ya definidas, y muestre las cadenas resultantes en la pantalla.

Para el encabezado, use las variables `first_name` y `greeting`, seguidas de una coma y un signo de exclamación. Muestre esto en la pantalla en el orden correcto.

Para el cuerpo del correo electrónico, use las variables `info` e `intro`, y asegúrese de que la segunda oración esté en una nueva línea.

El resultado en la pantalla se verá así:

<pre class='hexlet-basics-output'>
Hello, Joffrey!
Here is important information about your account security.
We couldn't verify your mother's maiden name.
</pre>

Complete la tarea utilizando solo dos `print()`.
