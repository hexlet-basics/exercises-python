
La función `my_substr()`, que implementaste en la lección anterior, contiene muchos errores. Pasó la prueba porque no había **casos límite**. La función funcionaba con argumentos normales. Pero ahora imaginemos que se le pasan estas longitudes:

* `0`
* Un número negativo
* Un número que excede la longitud real de la cadena

La función `my_substr()` no está preparada para estos casos. El código se ejecutará en diferentes situaciones, con diferentes combinaciones de condiciones y datos. No se puede estar seguro de que los argumentos siempre serán correctos, por lo que es necesario tener en cuenta todos los casos.

Los errores en los casos límite son una causa común de errores lógicos en los programas. Los programadores siempre olvidan algo. Estos errores a menudo no se manifiestan de inmediato y pueden no causar problemas visibles durante mucho tiempo.

El programa sigue funcionando, pero en algún momento se descubre que hay errores en los resultados. A menudo, la causa es la tipificación dinámica de Python.

Aprenderás a lidiar con estos errores con la experiencia.

Imaginemos una función extendida `my_substr()`. Toma tres argumentos: una cadena, un índice y la longitud de la subcadena a extraer. La función devuelve la subcadena de la longitud especificada, comenzando desde el índice especificado. Ejemplos de llamadas:

```python
string = 'If I look back, I am lost'
print(my_substr(string, 0, 1))  # => 'I'
print(my_substr(string, 3, 6))  # => 'I look'
```

Los siguientes **casos límite** deben tenerse en cuenta:

* Longitud negativa de la subcadena a extraer.
* Índice especificado negativo.
* El índice especificado está fuera de los límites de toda la cadena.
* La longitud de la subcadena, sumada al índice especificado, está fuera de los límites de toda la cadena.

Cuando se implementa la función, cada caso límite será un fragmento de código separado. Probablemente se implementará utilizando `if`.

Para escribir la función `my_substr()` y protegerse contra estos casos, es recomendable implementar una función separada que verifique la corrección de los argumentos.
