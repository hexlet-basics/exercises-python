
En su nivel más profundo, una computadora opera exclusivamente con los dígitos `0` y `1`. Esto se conoce como [código binario](https://es.wikipedia.org/wiki/C%C3%B3digo_binario), y los unos y ceros se llaman bits, abreviatura de "binary digit" (dígito binario).

Los números que estamos acostumbrados a utilizar en el sistema decimal se codifican utilizando números binarios:

- 0 ← 0
- 1 ← 1
- 2 ← 10
- 3 ← 11
- 4 ← 100
- 5 ← 101

Pero, ¿qué pasa con el texto? En realidad, la computadora no sabe nada acerca de las letras, signos de puntuación y otros caracteres de texto. Todos estos caracteres también se codifican con números.

Podemos tomar el alfabeto inglés y asignar un número a cada letra, comenzando desde uno en orden:

- a ← 1
- b ← 2
- c ← 3
- d ← 4
- ...
- z ← 26

Esto es lo que se conoce como **codificación**.

Durante el proceso de funcionamiento, los programas utilizan codificaciones para convertir números en caracteres y viceversa. Sin embargo, el programa en sí no tiene conocimiento del significado de estos caracteres.

- `hello` → `8` `5` `12` `12` `15`
- `7` `15` `15` `4` → `good`

Estas tablas que relacionan letras y números se llaman tablas de codificación. Además de las letras del alfabeto, las tablas de codificación incluyen signos de puntuación y otros caracteres útiles. Seguramente has encontrado tablas de codificación como [ASCII](https://es.wikipedia.org/wiki/ASCII) o [UTF-8](https://es.wikipedia.org/wiki/UTF-8).

Las distintas codificaciones contienen diferentes conjuntos de caracteres. Inicialmente, tablas pequeñas como ASCII eran suficientes para la realización de la mayoría de las tareas. Sin embargo, sólo incluían letras latinas, algunos caracteres simples como `%` y `?`, y caracteres de control especiales como el salto de línea.

Con la proliferación de las computadoras, diferentes países necesitaron elaborar propias tablas más amplias. Esto incluía letras cirílicas, caracteres chinos, árabe, matemáticos y tipográficos adicionales, y más tarde incluso emojis.

Hoy en día, en la mayoría de los casos se utiliza una de las variantes de [Unicode](https://es.wikipedia.org/wiki/Unicode), que incluye caracteres de casi todos los idiomas escritos del mundo.
