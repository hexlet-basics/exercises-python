Imagina que tenemos este programa:

```python
x = "Father!"
print(x)
```

Desde el punto de vista técnico todo funciona. Ya hemos visto ejemplos parecidos, pero aquí se usa una variable con el nombre `x`. Los nombres malos dificultan leer y entender el código. Aquí tienes algunos ejemplos de variables mal elegidas:

```python
a = "John"
n = 42
ddr = "New York"
```

¿Qué variables son estas? ¿Qué guardan? Para entenderlo hay que leer todo el resto del código y adivinar por el contexto.

Al ordenador le da igual cómo se llame una variable. Para él, `x`, `abc`, `message` o `elephant_in_the_room` son simplemente etiquetas para guardar datos. A las personas les importa otra cosa. Los programadores leen código bastante más a menudo de lo que lo escriben. Por eso los nombres de las variables son una parte importante de la comunicación a través del código.

## Buenos ejemplos

```python
user_name = "Arya Stark"
unpaid_orders_count = 3
max_attempts = 5
```

Un buen nombre de variable ayuda a entender qué hace el programa sin leer con detalle cada línea. Es especialmente importante dar nombres cuyo sentido se entienda sin contexto, sin necesidad de leer todo el código de alrededor.

Aquí tienes algunos consejos:

- Usa el inglés. Es el estándar internacional. Es mejor escribir `orders_count` que `cantidad_pedidos`. Si con el inglés todavía cuesta, usa un traductor: es normal. Con el tiempo se volverá más fácil.
- Procura que el nombre refleje el sentido de la variable. Que sea un poco más largo, pero comprensible.
- No temas gastar tiempo en elegir un buen nombre. Es una inversión en la legibilidad y el mantenimiento del código.

Entre los programadores hay incluso una broma: «Algunas de las tareas más difíciles en programación son la caché y inventar nombres para las variables». A veces inventar un nombre adecuado cuesta de verdad. Aquí tienes un ejemplo: ¿cómo llamarías a una variable que guarda la cantidad de pedidos sin pagar de clientes con deuda del trimestre anterior?

Y ahora un pequeño ejercicio: inventa un nombre para una variable que vaya a guardar «la cantidad de hermanos y hermanas del rey». Escríbelo en una nota o mándatelo por correo. Solo el nombre, sin explicaciones. Volveremos a esta tarea dentro de unas lecciones.
