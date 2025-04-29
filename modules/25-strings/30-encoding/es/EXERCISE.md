
En Python, puedes "solicitar" y mostrar en pantalla cualquier carácter de la codificación ASCII. Para hacer esto, se utiliza la función `chr()`. Por ejemplo:

```python
print(chr(63))
```


Se mostrará en pantalla el carácter con el número 63, que es el signo de interrogación `?`. De esta manera, puedes mostrar cualquier carácter.

Utiliza la [tabla de códigos ASCII](https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html). En esta tabla, nos interesa el código decimal (*dec* o *decimal*) con el que se codifican los caracteres.

Utilizando el ejemplo anterior y la tabla, muestra en pantalla (cada uno en su propia línea) `~`, `^` y `%`.

(Por supuesto, podrías "engañar" a las pruebas y simplemente hacer `print('~')`, etc., pero eso sería muy aburrido :)
