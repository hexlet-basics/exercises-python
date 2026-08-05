Los operadores de azúcar sintáctico resultan especialmente cómodos cuando hay que armar poco a poco el valor final.

Implementa la función `build_progress_bar()`, que recibe la cantidad de pasos completados y la cantidad total de pasos, y después devuelve una cadena-indicador del progreso.

Los pasos completados se marcan con el carácter `#` y los restantes con el carácter `-`. Procura no usar métodos incorporados de trabajo con cadenas en tu solución.

```python
build_progress_bar(0, 5)  # '-----'
build_progress_bar(3, 5)  # '###--'
build_progress_bar(5, 5)  # '#####'
```

Te será útil el operador `+=` para armar poco a poco la cadena nueva dentro del bucle `while`. Y también te servirá para gobernar la condición del bucle.
