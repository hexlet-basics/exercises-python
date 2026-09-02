En el nivel más básico, el ordenador trabaja solo con ceros y unos, lo que constituye el llamado código binario. Cada uno o cero se llama bit (de binary digit, «dígito binario»).

Cualquier dato en el ordenador está representado simplemente como una secuencia de bits: por ejemplo las imágenes, la música y el texto. Los números del sistema decimal que nos son habituales también se pueden representar en forma binaria.

- 0 → `0`
- 1 → `1`
- 2 → `10`

## ¿Cómo codificar texto?

El ordenador no «entiende» el texto. Para trabajar con las letras y otros caracteres, también hay que convertirlos en números. Eso se hace mediante codificaciones, es decir, tablas en las que a cada carácter le corresponde un número determinado.

La forma más simple consiste en numerar las letras empezando por 1.

- `a` → `1`
- `b` → `2`
- ...y así hasta `z` → `26`

Ahora podemos representar la palabra hello como un conjunto de números.

```text
h e l l o
↓ ↓ ↓ ↓ ↓
8 5 12 12 15
```

Y _good_ se convierte en esta secuencia.

```text
g o o d
↓ ↓ ↓ ↓
7 15 15 4
```

El programa no sabe que eso es una palabra. Simplemente ve la instrucción «hay que mostrar el carácter con el código 8, después el del código 5, etc.».

## ASCII. La primera codificación masiva

Los primeros ordenadores trabajaban principalmente con el inglés. Para él, en los años sesenta se ideó la tabla ASCII, que incluía 128 caracteres, entre ellos el alfabeto latino, las cifras, los signos de puntuación, los caracteres especiales (@, #, !, \n) y los códigos de control.

Eso bastaba para los primeros programas, pero no para todo el mundo.

Cuando los ordenadores empezaron a usarse en otros países, surgió un problema. En ASCII no hay caracteres cirílicos, ideogramas, escritura árabe, acentos, símbolos de moneda, etc.

Cada país o empresa empezó a hacer su propia codificación a partir de ASCII.

- Windows ideó Windows-1251 para el ruso
- Apple creó Mac Roman
- Los países de Europa del Este, Asia y Oriente Medio desarrollaron sus propias variantes

Todas esas codificaciones eran incompatibles entre sí. El código 226 en una codificación podía ser la letra é, en otra la letra и, y en una tercera un carácter técnico. Eso llevaba a un auténtico caos.

## Cómo se veían los problemas de codificación

Si ves en un texto esto.

```text
Â¡Hola, seÃ±or!
```

o

```text
?Hola, se?or!
```

Eso significa que el programa determinó mal la codificación del texto. Recibió una secuencia de bytes, pero los leyó con la tabla equivocada.

Eso era la norma en los años noventa y dos mil. Un programa escribía el texto en Windows-1252, otro lo leía como ISO-8859-1, y el resultado era basura.

## Unicode y UTF-8. El final del desorden

Para arreglarlo todo, en los años noventa se empezó a crear la tabla universal Unicode, que contiene los caracteres de todos los sistemas de escritura del mundo, entre ellos el alfabeto latino y el cirílico, la escritura china y árabe, los signos matemáticos, la escritura del antiguo Egipto e incluso los emojis.

Dentro de Unicode hay varios formatos de almacenamiento. El más extendido de ellos es UTF-8. Codifica de forma compacta los caracteres ingleses, pero puede ampliarse para cualquier otro.

Hoy UTF-8 es el estándar por defecto en internet, en Python, en Linux, en las bases de datos y en los editores de código.

## ¿Para qué necesita saber esto un programador?

- Trabajarás con texto, y los errores de codificación siguen ocurriendo, especialmente al leer archivos, procesar datos e interactuar con API y bases de datos.
- Python usa UTF-8 por defecto, pero a veces hay que indicar la codificación de forma explícita al leer archivos, por ejemplo `open('file.txt', encoding='utf-8')`.
- Hay que saber diagnosticar los problemas. Por ejemplo, si ves «caracteres raros», eso es casi con seguridad un error de codificación.
