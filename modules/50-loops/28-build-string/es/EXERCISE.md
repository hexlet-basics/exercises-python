
Implementa la función `my_substr()`, que extrae una subcadena de una cadena de longitud especificada. Recibe dos argumentos de entrada: la cadena y la longitud, y devuelve la subcadena comenzando desde el primer carácter:

Ejemplo de llamada:

```python
string = 'If I look back I am lost'
print(my_substr(string, 1)) # => 'I'
print(my_substr(string, 7)) # => 'If I lo'
```

Utiliza el mismo enfoque que en la función para invertir una cadena del tutorial: construye la cadena resultado en un bucle, recorriendo la cadena original hasta un punto determinado.

Esta tarea se puede resolver utilizando listas (slices). Pero en este ejercicio queremos practicar el uso de bucles, por lo que implementaremos esta funcionalidad por nuestra cuenta. Es así como funcionan internamente las listas.
