En matemáticas hay distintos tipos de números. Por ejemplo:

- Naturales: números enteros positivos: 1, 2, 3, etc.
- Racionales: números fraccionarios que se pueden representar como una división, por ejemplo: 0.5, 1.75, 3.14.

Desde el punto de vista de las matemáticas todo es simple. Pero desde el punto de vista del ordenador, entre esos tipos de números hay un auténtico abismo. Intenta resolver mentalmente: ¿cuánto es `0.2` + `0.1`? Evidentemente, `0.3`. Y esto es lo que dice Python:

```python
print(0.2 + 0.1)  # => 0.30000000000000004
```

En lugar del habitual 0.3 obtenemos 0.30000000000000004.

```text
Expectativa: 0.1 + 0.2  →  0.3
Realidad:    0.1 + 0.2  →  0.30000000000000004
                             └── error de almacenamiento
```

## ¿Por qué ocurre esto?

Este comportamiento es propio de JavaScript, C++ y la mayoría de los demás lenguajes de programación.

La causa está en la construcción del ordenador. El ordenador trabaja con una memoria limitada, mientras que los números racionales son infinitamente precisos. Entre 0.1 y 0.2 se pueden colocar infinitos otros números. Pero el ordenador no puede almacenar el infinito. Aproxima el número, intentando encajarlo en la cantidad de bits disponible.

Esos valores aproximados se llaman números de punto flotante (floating point numbers). Su almacenamiento y los cálculos con ellos obedecen a reglas estrictas, descritas en el estándar especial IEEE 754, al que se ajustan la mayoría de los lenguajes de programación.

## Cuándo aparecen esos números

Los números de punto flotante aparecen en los programas más a menudo de lo que puede parecer. Estos son los casos principales:

- Cuando escribes de forma explícita un número fraccionario, por ejemplo 0.1, 2.5, 3.14.
- Cuando realizas una división, incluso si divides dos números enteros:

```python
print(1 / 2)  # => 0.5
print(2 / 3)  # => 0.6666666666666666
```

Aunque el resultado parezca «bonito», por dentro está representado igualmente como un valor aproximado. Algunas fracciones, como 1 / 3, no se pueden representar de forma exacta en el sistema binario, por eso su precisión siempre está limitada.

## Dónde es crítico y cómo se trabaja con ello

Normalmente un error pequeño no molesta. Pero en los cálculos financieros, en las tareas científicas y de ingeniería, y también en la comparación exacta de resultados, puede convertirse en un problema. Por ejemplo, un error de una fracción de céntimo es capaz de dar un total incorrecto, y una cadena larga de cálculos puede acumular la imprecisión poco a poco.

En los programas reales esto se maneja de distintas maneras. El dinero se guarda a menudo en las unidades mínimas, por ejemplo en céntimos, es decir, se usan números enteros en lugar de fraccionarios. En otros casos el resultado se redondea a la cantidad de decimales necesaria, se comparan los números con un error admisible o se usan tipos de datos y bibliotecas especiales para cálculos exactos.

## Qué hay que recordar

Las operaciones con números de punto flotante no siempre son exactas, y eso es normal. Ese comportamiento es propio de la mayoría de los lenguajes de programación y se explica por la construcción de la memoria del ordenador. La precisión se puede controlar, por ejemplo mediante el redondeo o comparando los números con un error dado. Y al trabajar con dinero, con medidas exactas o con cálculos científicos, es mejor usar tipos de datos especiales que garanticen el control sobre la precisión.
