
El orden de las instrucciones en el código con variables es de gran importancia. Por lo tanto, la variable debe ser definida antes de su primer uso. A continuación, se muestra un ejemplo de error que cometen con frecuencia los principiantes:

```python
print(greeting)
greeting = 'Father!'
```

La ejecución del programa anterior termina con el error `NameError: name 'greeting' is not defined` — este es un error de referencia. Esto significa que en el código se está utilizando un nombre (identificador) que aún no ha sido definido. Esto se indica en el propio texto del error: `'greeting' is not defined`. Además del orden incorrecto de las acciones, en Python también se encuentran errores tipográficos en el nombre de la variable. Esto ocurre tanto cuando se utiliza la variable como cuando se la declara.

La cantidad de errores similares se puede reducir si se utiliza un editor correctamente configurado. Este editor advierte sobre posibles problemas y resalta las variables que se utilizan sin ser declaradas.
