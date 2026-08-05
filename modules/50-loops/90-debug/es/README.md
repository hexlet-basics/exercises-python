Incluso a los desarrolladores más experimentados el código rara vez les funciona a la perfección la primera vez. Cuanto más experimentado es el desarrollador, con más seguridad lo **depura**, es decir, analiza los errores y los elimina.

La habilidad de depurar no aparece por sí sola. Hay que desarrollarla, y además lo antes posible. A lo largo del aprendizaje harás ejercicios y practicarás, y con el tiempo el análisis de los errores se convertirá en un hábito.

## Cómo encontrar el error en el código

Depurar a base de prueba y error lleva mucho tiempo. Es mucho más productivo entender primero qué fue exactamente lo que salió mal y luego eliminar la causa. Cualquier trabajo con errores empieza por la comprensión.

Lo primero es estudiar el **traceback**. El traceback contiene la lista de todas las llamadas a funciones desde el arranque del programa hasta el lugar del error. Por él se ve qué funciones se ejecutaron con éxito y dónde surgieron los problemas. Cada registro indica el archivo, la línea y la función que se estaba ejecutando.

Imaginemos que escribiste código en el archivo `users.py` y llamaste a la función `main()` en la cuarta línea. El registro en el traceback se verá así:

```bash
File "users.py", line 4, in <module>
  main()
```

Aquí se ve no solo el archivo y la línea, sino también el nombre del módulo. Por él se puede determinar si el problema surgió en tu código o en una biblioteca de terceros.

Cuando el traceback llega al lugar problemático, muestra un **mensaje de error**. Por ejemplo:

```bash
NameError: name 'create' is not defined
```

El mensaje dice que el nombre `create` no está definido. Ese error significa, la mayoría de las veces, un error tipográfico en el nombre. Si tu inglés todavía no es muy bueno, te ayudará un traductor.

Juntos, el traceback y el mensaje de error se ven así:

```bash
Traceback (most recent call last):
  File "users.py", line 4, in <module>
    main()
  File "users.py", line 2, in main
    create()
NameError: name 'create' is not defined
```

Toda la cadena de sucesos se ve de golpe. El programa llegó con éxito hasta `main()`, después pasó a `create()` y aquí se topó con un error en el nombre.

## Tipos de errores

Los errores más comprensibles en Python se llaman **sintácticos**. Surgen cuando el código está escrito incorrectamente, por ejemplo por una comilla equivocada o un paréntesis omitido. En la salida siempre está presente `SyntaxError:`.

Miremos un ejemplo. Aquí hay un error sintáctico debido a que la comilla de apertura `"` no coincide con la de cierre `'`:

```bash
Traceback (most recent call last):
  File "users.py", line 2
    print("Hello" + "world')
                           ^
SyntaxError: EOL while scanning string literal
```

Lo más difícil de corregir son los **errores de programación**. Aquí entran la llamada a una función que no existe, el uso de una variable no declarada y el paso de argumentos de tipo incorrecto. Normalmente surgen no en el lugar donde está la causa real, lo que complica el diagnóstico.

Con lo más difícil de luchar es con los **errores lógicos**. El programa funciona sin excepciones, pero da un resultado incorrecto con algunos datos de entrada. No hay ningún mensaje de error, solo una salida inesperada. Por ejemplo, la función debe calcular la suma, pero calcula la diferencia:

```python
# La función debe calcular la suma de los números, pero calcula la diferencia:
def sum(a: int, b: int) -> int:
    return a - b


# Con esa llamada el error no es evidente, porque
# tanto con la suma como con la resta el resultado será el mismo
sum(4, 0)  # 4
```

## Formas de depurar

En la base de cualquier método de depuración está la observación de las variables durante la ejecución. Miremos una función concreta.

Abajo hay una función que calcula la suma de los números desde `start` hasta `finish`. Con `start=3` y `finish=5` debe calcular `3 + 4 + 5`.

```python
def sum_of_series(start: int, finish: int) -> int:
    result = 0
    n = start
    while n < finish:
        result = result + n
        n = n + 1
    return result
```

En la función, las variables clave son `n` y `result`. Para encontrar el error hay que ver qué valores toman en cada iteración.

Para eso existen los **depuradores visuales**. Se integran en los editores de código populares y permiten ejecutar el programa paso a paso, observando las variables en tiempo real. Se puede encontrar uno adecuado buscando «Python debuggers» en Google.

En Hexlet, en lugar de un depurador se usa la **impresión de depuración**. El principio es el mismo, solo que los valores de las variables se muestran con el `print` normal. Lo que se imprime se ve en la pestaña `OUTPUT`.

```python
def sum_of_series(start: int, finish: int) -> int:
    result = 0
    n = start
    while n < finish:
        print("new iteration !!!!")
        print(n)
        result = result + n
        n = n + 1
        print(result)
    return result


sum_of_series(3, 5)

# new iteration !!!!
# 3
# 3
# new iteration !!!!
# 4
# 7
```

La salida muestra que hay una iteración menos de las necesarias. El cinco (`finish`) no entró en la suma. En la condición está `n < finish` en lugar de `n <= finish`. Hay que cambiar el signo `<` por `<=`.

Los desarrolladores que empiezan a menudo se disgustan por los errores y se consideran poco atentos. Errores tienen todos, tanto los juniors como los seniors. La diferencia está en con cuánta seguridad los encuentras.

Los principiantes piensan que un buen desarrollador mira el código y entiende de inmediato qué va mal. Eso rara vez funciona en la práctica. Un fragmento de código sin contexto dice poca cosa. **Si quieres pedir consejo a un desarrollador experimentado, lo primero es mostrarle el mensaje de error.**
