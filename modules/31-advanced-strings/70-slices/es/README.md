Al trabajar con cadenas nos encontramos a menudo con una tarea: extraer una parte de la cadena. Por ejemplo, obtener el año de una fecha, el nombre de un nombre completo o los primeros caracteres de una dirección de correo electrónico. Para esos casos, en Python existe una herramienta potente y cómoda: los cortes (o slices).

## ¿Qué es una subcadena?

Una subcadena es una parte de una cadena. Lo que está contenido dentro de otra cadena. Por ejemplo, en la cadena '12-08-2034' una subcadena puede ser '2034', '12' o incluso '-'. Todo depende de qué información necesitemos extraer.

Supongamos que tenemos una cadena con la fecha '12-08-2034'. Queremos obtener de ella solo el año, '2034'. En esta cadena cada carácter tiene un índice (una posición), empezando por cero:

```text
'1' '2' '-' '0' '8' '-' '2' '0' '3' '4'
 0   1   2   3   4   5   6   7   8   9
```

Resulta que el año empieza en el índice 6 y termina en el 9. Para extraerlo usamos un corte:

```python
value = "12-08-2034"
year = value[6:10]
print(year)  # => 2034
```

El corte `value[6:10]` toma los caracteres desde el índice 6 hasta el 9 inclusive. El formato del corte:

```python
cadena[inicio:fin]
```

El carácter cuyo índice se indica como «fin» no se incluye. Se puede entender como el orden natural del carácter que hay que tomar como último. Es decir, si ahí está el 11, significa que será el carácter número 11 por orden.

```python
# El último carácter tiene el índice 10, y en total hay 11 letras
value = "code-basics"

print(value[5:11])  # => basics (del índice 5 al 10)
print(value[0:7])  # => code-ba (del índice 0 al 6)
print(value[2:6])  # => de-b
print(value[:4])  # => code
print(value[5:])  # => basics
```

¿Cómo se cuenta todo esto? Si trabajamos con una cadena concreta, casi siempre se hace a ojo.

## El corte es una cadena

```python
value = "01-12-9873"

value[1:2]  # => 1
value[3:5]  # => 12
```

Un corte siempre devuelve una cadena, incluso si dentro solo hay dígitos. Eso significa que el resultado se puede usar como una cadena normal: concatenarlo, imprimirlo, pasarlo a funciones y así sucesivamente.

```python
part = value[3:7]  # => 12-9
print(part[0:2])  # => 12
```

Primero obtuvimos la subcadena `'12-9'`, y después hicimos de ella un nuevo corte, `'12'`.

## Corte hasta el final o desde el principio

A veces hay que tomar una parte de la cadena hasta el final o desde el principio. Esas situaciones también se resuelven con facilidad mediante cortes:

```python
value = "Hexlet"

print(value[3:])  # => let     # Del carácter 3 al final
print(value[:3])  # => Hex     # Del principio al carácter 3
```

Si no se indica el límite, Python pondrá por su cuenta el valor necesario: el principio de la cadena o su final.

## ↩ Cortes con índices negativos

Python permite contar de izquierda a derecha y desde el final de la cadena. Para eso se usan los índices negativos.

```python
value = "Hexlet"

print(value[-1])  # => t      # El último carácter
print(value[3:-1])  # => le     # Del 3 al penúltimo
print(value[-5:3])  # => ex     # Del 1 al 2
```

El índice `-1` en este caso corresponde al último carácter de la cadena. Por eso aquí vemos un resultado distinto:

```python
print(value[3:-1])  # => le
print(value[3:])  # => let
```

Es cómodo cuando no se conoce de antemano la longitud de la cadena, pero hay que tomar la «cola» o la «parte media» de la cadena respecto al final.

## El paso en los cortes

El corte tiene un tercer parámetro llamado paso. Por defecto el paso es igual a 1, es decir, los caracteres van seguidos. Pero el paso se puede cambiar, por ejemplo para tomar cada segundo carácter:

```python
value = "Hexlet"

print(value[1:5:2])  # => el
# Índices 1, 3 → caracteres e, l
```

En este ejemplo:

- 1:5 define el corte 'exle'
- el paso 2 significa que tomamos un carácter de cada dos: 'e' y 'l'

Se puede combinar con límites abiertos:

```python
print(value[:5:2])  # => Hxe
print(value[1::2])  # => elt
```

## Invertir una cadena

El paso negativo permite invertir una cadena, lo que es uno de los «trucos» más populares de los cortes. Para eso se usa un paso negativo:

```python
value = "Hexlet"

print(value[::-1])  # => telxeH
```

La cadena se lee del final al principio. Muy cómodo y conciso.

## Cortes con paso negativo

Si usas un paso negativo, recuerda: los índices también hay que indicarlos en orden inverso. Si no, el corte no funcionará (devolverá una cadena vacía):

```python
value = "Hexlet"

print(value[4:1:-1])  # => elx
# Índices: 4, 3, 2 → e, l, x
```

Python empezará por el índice 4 e irá hacia la izquierda hasta el índice 2 inclusive. El índice 1 no entra en el resultado.

## Corte con variables

Los cortes no tienen que estar fijados con números. Se pueden usar variables:

```python
start = 1
end = 5

value = "Hexlet"
print(value[start:end])  # => exle
```

Esto resulta especialmente útil cuando los límites se calculan durante la ejecución del programa.

## Chuleta rápida

```python
value = "Hexlet"

value[::]  # Hexlet  — la cadena completa
value[:]  # Hexlet
value[::2]  # Hxe     — los caracteres pares
value[1::2]  # elt     — los caracteres impares
value[::-1]  # telxeH  — la cadena en orden inverso
value[5:]  # t
value[:5]  # Hexle
value[-2:1:-1]  # elx     — del penúltimo al tercero
```

Cuando hagas un corte de un índice mayor a uno menor, define obligatoriamente un paso negativo, porque si no el corte no funcionará.

No te preocupes si ahora no memorizas todas las combinaciones: empezarás a usarlas en la práctica muy pronto. Lo principal es entender cómo funciona la estructura básica `cadena[inicio:fin:paso]`.
