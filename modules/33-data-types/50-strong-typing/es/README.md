Python es un lenguaje de tipado estricto (o fuerte) y se toma los tipos de datos muy en serio. Al intentar ejecutar una operación entre tipos incompatibles, el programa lanzará un error.

## ¿Qué significa eso en la práctica?

Supongamos que sumas dos números:

```python
print(1 + 7)  # => 8
```

Todo perfecto. La operación de suma está permitida para los números, así que el programa funcionará y mostrará en pantalla *8*. ¿Y qué pasará si intentamos sumar un número y una cadena?

```python
print(1 + '7')
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Python informa de que no puede sumar int y str. Es un error de tipos: los valores pertenecen a categorías distintas y el programa se niega a continuar.

```text
'2' + 1

str + int → TypeError!

Hace falta una conversión:
int('2') + 1 → 3
'2' + str(1) → '21'
```

## ¿Por qué tan estricto?

Python te protege de errores poco evidentes y peligrosos. Exige que indiques explícitamente cómo quieres convertir los datos:

- o convertir la cadena en número (`int('7')`);
- o convertir el número en cadena (`str(1)`).

Aprenderemos a hacerlo un poco más adelante.

## Cuándo Python convierte los tipos por sí mismo

Si en una misma expresión aparecen un número entero y uno real, Python convierte el entero a real automáticamente.

```python
print(1 + 1.5)  # => 2.5
```

El entero `1` se convierte en `1.0` y el resultado sale `2.5`. Funciona porque cualquier número entero se representa exactamente como real: los datos no se pierden. Python lo sabe y hace la conversión él mismo (como la mayoría de los demás lenguajes).

## ¿Y cómo es en otros lenguajes?

No todos los lenguajes son así. Por ejemplo, PHP y JavaScript usan tipado débil. Convierten los tipos automáticamente cuando lo consideran "razonable".

```javascript
1 + '7';  // => '17'
```

En este ejemplo, el número 1 se convierte implícitamente en la cadena '1' y el resultado pasa a ser '17'.

Ese comportamiento apareció por razones bastante objetivas. En muchos lenguajes, sobre todo en los que se usan a menudo en desarrollo web, el programa tiene que trabajar constantemente con datos que vienen de fuera. Por ejemplo, los valores de los formularios HTML, de los parámetros de la URL o de las peticiones HTTP llegan a menudo como cadenas, aunque por su sentido sean números. En PHP, por ejemplo, una cadena con un número puede participar automáticamente en la aritmética como número:

```php
'7' + 1; // 8
```

Hay también otros lenguajes con sus propias reglas. Por ejemplo, en Ruby el comportamiento en este punto se parece más al de Python: la expresión `1 + '7'` no se considera admisible. Y el lenguaje C también permite algunas conversiones implícitas, pero ya por sus propias reglas, más de bajo nivel. En la práctica, sin embargo, esto lleva a tales problemas que los lenguajes modernos han renunciado a esas licencias. Esos errores son especialmente difíciles de detectar, porque el comportamiento del programa depende del tipo de datos que le llegaron. A veces todo funciona y a veces no.

Además, los lenguajes no se dividen exactamente en dos bandos: "estrictos" y "débiles". Es más correcto decir que los distintos lenguajes tienen distintos grados de rigor. En unos las conversiones implícitas casi no existen y en otros son bastante más numerosas.

## Tipado estático y dinámico

Existe otro concepto aparte: el tipado estático y el dinámico. Describe cuándo y cómo se comprueban los tipos en el lenguaje. Python pertenece a los lenguajes de tipado dinámico: aquí los tipos se comprueban durante la ejecución del programa. En los lenguajes de tipado estático esa comprobación suele ocurrir antes, incluso antes de ejecutar el código, en la etapa de compilación.

El tipado estricto y el débil describen ya otra propiedad del lenguaje: con qué facilidad el lenguaje realiza conversiones implícitas entre tipos distintos. Es importante no confundirlo con el tipado estático y dinámico. Un término responde a la pregunta "cuándo se comprueban los tipos" y el otro a la pregunta "qué ocurrirá si se mezclan tipos distintos sin una conversión explícita".

## Conclusión

Python es un lenguaje de tipado estricto. No permite ejecutar operaciones entre tipos incompatibles sin una conversión explícita. Eso hace que los programas sean más fiables y más claros. Todavía aprenderemos a convertir los datos de un tipo a otro y a hacerlo siempre de forma consciente.
