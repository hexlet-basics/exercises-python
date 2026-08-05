A veces en un programa aparecen valores que nunca deben cambiar. Por ejemplo:

- La constante matemática π (pi).
- El tipo de cambio del dólar en una fecha determinada.
- La comisión fija de un servicio.

Esos valores se llaman constantes y se acostumbra a distinguirlos de las variables normales, para que no surja la tentación de cambiarlos.

## Ejemplo: el número π

```python
PI = 3.14
print(PI)  # => 3.14
```

Aquí PI es una constante que guarda el valor del número π. El sentido de una constante es que su valor no debe cambiar durante el funcionamiento del programa.

## ¿En qué se diferencia una constante de una variable?

El concepto de constante está extendido en la mayoría de los lenguajes de programación. Allí la constante es a menudo una entidad aparte del lenguaje, cuyo valor no se puede modificar. En Python las constantes como concepto aparte del lenguaje no existen, pero hay un acuerdo: si una variable está escrita con letras en mayúscula, es una constante.

```python
PI = 3.14
PI = 3.14159  #  Técnicamente es posible, pero no se acostumbra a hacerlo
```

Pero por convención, si una variable está nombrada con letras mayúsculas, se considera una constante y no se debe cambiar.

## Cómo se formatean las constantes

- Todas las letras en mayúscula
- Las palabras se separan con el carácter de subrayado `_`
- El estilo se llama UPPER_SNAKE_CASE (también se lo llama SCREAMING_SNAKE_CASE)

```python
PI = 3.14
MAX_USERS = 100
DEFAULT_TIMEOUT = 30
```

## ¿Para qué hacen falta las constantes?

Las constantes hacen el código más claro y más seguro. Ayudan a ver de inmediato qué valores del programa se consideran fijos y no deben cambiar. Eso es especialmente importante al trabajar con datos como las constantes matemáticas y físicas, los ajustes por defecto o los límites fijos. El uso de constantes reduce el riesgo de errores: por el nombre de la variable se entiende de inmediato que tenemos delante una constante y que no conviene cambiarla. Además, si el valor hay que cambiarlo de todos modos (por ejemplo, en los ajustes), basta con modificarlo en un solo lugar y el cambio se recogerá automáticamente en todo el programa.
