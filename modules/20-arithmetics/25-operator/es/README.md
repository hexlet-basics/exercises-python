En matemáticas y en programación usamos a menudo signos de operaciones, como `+`, `-`, `*` y otros. En programación esos signos se llaman operadores.

- Un operador es un símbolo o una palabra que denota una acción.
- Los operandos son los valores a los que se aplica el operador.

Un ejemplo:

```python
print(8 + 2)
```

Aquí:

- `+` es el operador
- `8` y `2` son los operandos
- el resultado será `10`

```text
operando  operador  operando       resultado
    8         +          2       →      10
    5         -          3       →      2
    4         *          3       →      12
```

## Operadores unarios

Existen también las operaciones unarias, que trabajan con un solo operando. Un ejemplo:

```python
print(-3)  # => -3
```

En este caso `-` es un operador unario y `3` es el operando. El intérprete recibe la orden: «toma el número 3 y cambia su signo».

El operador `-` se puede usar de distintas maneras. Cuando está **entre dos números**, es la operación de resta:

```python
print(5 - 2)   # => 3
print(10 - 7)  # => 3
```

Aquí `-` toma el primer número y le resta el segundo.

Esa diferencia se nota especialmente al trabajar con números negativos. Por ejemplo:

```python
# menos por menos da más
print(5 - -2) # => 7
```

Primero vemos la operación de resta: `5 - (...)`. Pero a la derecha está el menos unario `-2`, que convierte el `2` en un número negativo. Al final resulta: `5 - (-2) = 7`.

Así, el significado de `-` depende del contexto: si al lado hay otro número, es una resta; si no, es un cambio de signo del número.

Lo principal que hay que recordar aquí es que el comportamiento e incluso la propia escritura corresponden por completo a cómo lo hacíamos en la escuela.

## Errores en los cálculos y en el análisis

Si se percibe `-3` como un número único, se puede no notar que `-` es un operador aparte con su propia prioridad. Por ejemplo:

```python
print(-3**2)
```

A primera vista puede parecer que se eleva al cuadrado `-3` y que el resultado debería ser `9` (cualquier número al cuadrado se vuelve positivo). Pero el resultado será `-9`.

La cuestión está en el orden de los cálculos: primero se realiza la potenciación (`**`) y solo después se aplica el menos unario. Es decir, el programa calcula así: `-(3**2) = -9`. De la prioridad de las operaciones hablaremos en detalle más adelante en el curso.
