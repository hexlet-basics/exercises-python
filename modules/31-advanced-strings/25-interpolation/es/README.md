Recordemos cómo funciona la concatenación. Para ello unimos las cadenas necesarias (o las variables con cadenas dentro) mediante el signo `+`.

```python
first_name = 'Joffrey'
greeting = 'Hello'

print(greeting + ", " + first_name + "!")
# => Hello, Joffrey!
```

Pero, al mismo tiempo, en expresiones complejas cuesta ver de inmediato qué texto se obtendrá al final. Sobre todo si en la cadena hay espacios, comas o comillas: empiezan a estorbar la lectura. Incluso el ejemplo actual exige un pequeño esfuerzo para entender cómo saldrá la cadena.

Por esa razón, en muchos lenguajes existe una operación llamada interpolación. La interpolación es una forma de insertar los valores de las variables directamente dentro de una cadena. En Python para eso se usan las f-strings (o cadenas de formato). Así:

```python
first_name = 'Joffrey'
greeting = 'Hello'

print(f'{greeting}, {first_name}!')
# => Hello, Joffrey!
```

La letra f delante de las comillas indica que dentro de la cadena se pueden usar variables. Sus nombres se escriben entre llaves, y Python sustituye automáticamente los valores necesarios.

```text
first_name = 'Joff'
greeting   = 'Hello'

f'{greeting}, {first_name}!'
   └───┬───┘  └────┬─────┘
   'Hello'    'Joff'
    └──────┬───────┘
    'Hello, Joff!'
```

Compara estos dos ejemplos uno al lado del otro:

```python
print(greeting + ", " + first_name + "!")
print(f'{greeting}, {first_name}!')
```

La segunda variante es más simple y más clara.

## Ejemplo

```python
school = 'Hexlet'

what_is_it = f'{school} - online courses'
print(what_is_it)  # => Hexlet - online courses
```

Esa forma de escribir se lee con facilidad: los espacios, los guiones y los símbolos se ven de inmediato. La cadena se parece exactamente a como aparecerá en la salida. Eso hace que el código sea claro y cómodo de mantener. Por esa razón, en la mayoría de los lenguajes la interpolación es preferible a la concatenación.

## Por qué esto importa

La interpolación es preferible a la concatenación en casi todos los lenguajes de programación modernos. Ella:

- Simplifica la estructura de las cadenas.
- Mejora la legibilidad del código.
- Reduce la cantidad de errores al trabajar con espacios y signos de puntuación.
