Implementa la función `compress(string)`, que comprime una cadena con el método RLE (Run-Length Encoding).

El algoritmo: si un carácter se repite varias veces seguidas, se reemplaza por el carácter y la cantidad de repeticiones. Los caracteres que aparecen una sola vez se escriben sin número.

Ejemplos:

```python
compress("aaabcccc")  # "a3bc4"
compress("abcd")  # "abcd"
compress("aabbaa")  # "a2b2a2"
compress("")  # ""
```

Este algoritmo se usa en formatos reales de compresión de datos, por ejemplo en los antiguos protocolos de fax y en los archivos BMP.

### Algoritmo

1. Recorrer la cadena contando la cantidad de caracteres iguales consecutivos
2. En cuanto el carácter cambie, escribir el carácter anterior y el contador (si es mayor que 1)
3. No olvidar procesar el último grupo después de terminar el bucle
