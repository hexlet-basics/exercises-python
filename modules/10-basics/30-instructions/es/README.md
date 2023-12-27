Cuando preparamos una comida, seguimos la receta al pie de la letra. De lo contrario, la comida no saldrá como esperábamos. Esta regla también se aplica a la programación.

Para ver el resultado esperado en la pantalla, es necesario darle al ordenador instrucciones claras, paso a paso. Una instrucción es un comando para el ordenador; una unidad de ejecución. En este caso, el código en Python es un conjunto de instrucciones. Se puede representar como una receta de cocina paso a paso.

El código en Python es ejecutado por un **intérprete** - es decir, un programa que ejecuta las instrucciones recibidas en orden. Al igual que los pasos en una receta, el conjunto de instrucciones para el intérprete se escriben en orden y se separan por saltos de línea.

Los desarrolladores deben entender el orden de las acciones en el código y ser capaces de dividir mentalmente el programa en partes independientes, fáciles de analizar.

Veamos un ejemplo de código con dos instrucciones. Al ejecutarlo, se mostrarán en la pantalla dos frases en secuencia:

```python
print('Mother of Dragons.')
print('Dracarys!')
# => Mother of Dragons.
# => Dracarys!
```

https://replit.com/@hexlet/python-basics-instructions

Anteriormente hemos señalado que las instrucciones se separan por saltos de línea. Pero también hay otra forma: se pueden separar por punto y coma (`;`):

```python
print('Mother of Dragons.'); print('Drakarys!')
```

No hay diferencia técnica alguna entre la primera y la segunda opción: el intérprete entenderá las instrucciones de la misma manera. La única diferencia es que la segunda opción puede ser incómoda de leer para los humanos.

Es mejor colocar las instrucciones una debajo de la otra. De esta manera, será más fácil para tus colegas leer tu código, mantenerlo y realizar cambios en él.
