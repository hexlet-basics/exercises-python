
Si un programa escrito en Python tiene errores de sintaxis, el intérprete mostrará un mensaje correspondiente en la pantalla. También indicará el archivo y la línea donde se produjo el error.

Un **error de sintaxis** ocurre cuando el código se ha escrito con violación de las reglas gramaticales. En los lenguajes naturales, la gramática es importante, pero generalmente se puede entender y leer el texto con errores. En la programación, todo es estricto. El más mínimo error y el programa ni siquiera se ejecutará. Un ejemplo puede ser un punto y coma olvidado, paréntesis mal colocados y otros detalles.

Aquí hay un ejemplo de código con un error de sintaxis:

```python
print('Hodor)
```


Si ejecutamos el código anterior, veremos el siguiente mensaje:

```bash
python index.py
File "index.py", line 1
  print('Hodor)
              ^
SyntaxError: EOL while scanning string literal
```

Por un lado, los errores de sintaxis son los más simples, porque están relacionados con las reglas gramaticales de escribir código, no con el significado del código. Son fáciles de corregir: solo necesitas encontrar la violación en la escritura. Por otro lado, el intérprete no siempre puede señalar claramente esta violación. Por lo tanto, a veces es necesario colocar el paréntesis olvidado no donde indica el mensaje de error.
