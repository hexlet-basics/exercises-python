En esta lección estudiaremos los parámetros opcionales de las funciones. Aprenderemos a leer una firma y la descripción del resultado en la documentación. Practicaremos las llamadas con argumentos obligatorios y opcionales.

Cuando una función tiene un valor por defecto para un parámetro, podemos omitir su argumento al llamarla. Si lo omitimos, la función utiliza ese valor. La firma indica qué parámetros tienen valores por defecto.

Veamos la función incorporada `round()`, que redondea un número:

```python
result = round(10.25, 0)  # 10.0
```

Le pasamos dos valores:

- El número que hay que redondear.
- La precisión del redondeo; `0` significa que el redondeo será hasta el número entero.

Como lo que se necesita con más frecuencia es precisamente el redondeo al entero, los creadores de la función `round()` hicieron el segundo parámetro opcional: si no se indica (el valor por defecto es `None`), el redondeo también se hace hasta el entero. Solo cambia la forma del resultado: con `0` es `10.0` y sin el segundo argumento es `10`:

```python
result = round(10.25)  # 10
```

Si hace falta otra precisión, se puede indicar explícitamente:

```python
# redondeo a un decimal
result = round(10.25, 1)  # 10.2
```

```text
round(10.25, 1)  →  argumentos: 10.25, 1       →  10.2
round(10.25)     →  argumentos: 10.25, (None)  →  10
                                        └── valor por defecto
```

En la firma de `round()`, el parámetro obligatorio `number` aparece antes del opcional `ndigits`. Otra función puede tener una cantidad distinta de parámetros y otros valores por defecto.

## Cómo leer la documentación de una función

La documentación explica qué datos acepta una función y qué resultado devuelve. La firma que aparece al principio de la referencia muestra el nombre de la función, sus parámetros y su orden. El texto que viene después explica el propósito de los parámetros y el comportamiento de la función. Para preparar una llamada, necesitamos ambas partes.

Veamos la [referencia de `round()`](https://docs.python.org/3/library/functions.html#round). Empieza con la firma `round(number, ndigits=None)`. Los nombres `number` y `ndigits` representan parámetros. En una llamada los sustituimos por valores concretos, por ejemplo `round(10.25, 1)`.

La tabla relaciona las partes de la firma con los argumentos de esa llamada.

| Parte de la firma | Significado | En la llamada `round(10.25, 1)` |
| --- | --- | --- |
| `round` | Nombre de la función | Llamamos a `round()` |
| `number` | Parámetro obligatorio, el número que se redondea | Pasamos `10.25` |
| `ndigits=None` | Parámetro opcional cuyo valor por defecto es `None` | Pasamos `1` en lugar del valor por defecto |

El signo `=` en `ndigits=None` indica un valor por defecto. Esta notación muestra que podemos omitir el segundo argumento. El texto bajo la firma explica cómo usa la función ese valor `None`. En `round()`, omitir el segundo argumento significa redondear al entero.

La descripción del resultado empieza bajo la firma. La palabra inglesa `return` significa «devolver». La referencia de `round()` explica que la función devuelve un número redondeado a la cantidad indicada de posiciones después del separador decimal. También aclara que, sin `ndigits`, el resultado será un entero. La firma muestra una llamada válida y la descripción permite entender el resultado.

Probemos ambos casos en el intérprete interactivo de Python (REPL). Los signos `>>>` indican el indicador del intérprete; las líneas que siguen a las llamadas muestran el resultado.

```console
>>> round(10.25, 1)
10.2
>>> round(10.25)
10
```

Aquí, la primera llamada pasa la precisión `1` y obtiene `10.2`. La segunda conserva el valor por defecto de `ndigits` y obtiene el entero `10`. Así relacionamos la firma, la explicación de la documentación y el resultado de la ejecución.

## Notación en la referencia

Una referencia puede incluir símbolos especiales. Ayudan a leer la firma y no se pasan a la función en una llamada.

| Notación en la referencia | Cómo interpretarla |
| --- | --- |
| `round(number, ndigits=None)` | `ndigits` tiene un valor por defecto, por lo que podemos omitir el argumento |
| `round(number[, ndigits])` | Otra forma de indicar un argumento opcional en una referencia. Los corchetes no forman parte de la llamada |
| `abs(number, /)` | El parámetro anterior a `/` recibe su argumento por posición. El signo `/` no es otro parámetro |

Por ejemplo, `abs(number, /)` describe una función con un parámetro. La llamada `abs(-5)` le pasa el número `-5` y devuelve `5`. Ni el nombre `number` ni el signo `/` se copian en esa llamada.

Si el navegador traduce la página, hay que comparar los nombres de las funciones, los parámetros y los símbolos de la firma con el original. El código utiliza los nombres originales de la documentación. Por ejemplo, traducir `number` como «número» ayuda a entender la descripción, pero en la llamada seguimos pasando el valor `10.25`.

## Trabajar con una función desconocida

Leemos una referencia para resolver una tarea. Por ejemplo, para redondear un precio a una posición decimal, buscamos el número y la precisión en la firma de `round()`, comprobamos el significado de la precisión en la descripción y probamos `round(10.25, 1)`. Si el resultado corresponde a la descripción, podemos usar esa llamada en el programa.

Otra función tendrá sus propios parámetros y reglas. Su firma nos indica qué argumentos pasar, la descripción explica el resultado y las restricciones, y un ejemplo pequeño nos permite comprobar lo que entendimos.
