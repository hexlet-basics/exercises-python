El programa prepara el texto de las notificaciones: quita los caracteres innecesarios del principio y repite el mensaje la cantidad de veces necesaria. Implementa la función `trim_and_repeat()`, que recibe tres parámetros:

* Una cadena
* `offset`: la cantidad de caracteres que hay que recortar de la cadena por la izquierda
* `repetitions`: cuántas veces hay que repetir la cadena antes de devolver la cadena resultante

La cantidad de caracteres del corte por defecto es 0, y la cantidad de repeticiones por defecto es 1.

La función debe devolver la cadena obtenida.

  ```python
  text = "python"

  trim_and_repeat(text, offset=3, repetitions=2)  # honhon
  trim_and_repeat(text, repetitions=3)  # pythonpythonpython
  trim_and_repeat(text)  # python
  ```

## Pistas

* Esta función se puede implementar de varias maneras
* Desde el punto de vista del sistema de comprobación no importa de qué manera se implemente por dentro la función `trim_and_repeat()`. Lo principal es que cumpla la tarea planteada
