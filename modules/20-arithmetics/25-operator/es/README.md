
Un **operador** es un símbolo de operación, como `+`. Los operadores realizan operaciones en función de valores específicos, llamados **operandos**. Los operadores en sí suelen ser uno o varios caracteres, aunque en ocasiones pueden ser también una palabra. La gran mayoría de los operadores corresponden a operaciones matemáticas.

```python
print(8 + 2)
```

En este ejemplo, `+` es el operador y los números `8` y `2` son los **operandos**.

Cuando sumamos, tenemos dos operandos: uno a la izquierda y otro a la derecha del signo `+`. Las operaciones que requieren dos operandos se llaman **binarias**. Si falta al menos un operando, por ejemplo, `3 +`, el programa dará un error de sintaxis.

Las operaciones no sólo pueden ser binarias; también pueden ser unarias, con un solo operando, o ternarias, con tres operandos. Además, los operadores pueden tener la misma apariencia pero representar operaciones diferentes. Los símbolos `+` y `-` no solo se utilizan como operadores. Cuando se trata de números negativos, el signo menos forma parte del número:

```python
print(-3)  # => -3
```

En el ejemplo anterior, se aplica una operación unaria al número `3`. El operador menos antes del tres le indica al intérprete que tome el número `3` y encuentre su opuesto, es decir, `-3`. Esto puede resultar confuso, ya que `-3` es tanto un número en sí mismo como un operador con un operando. Sin embargo, esta es la estructura que tienen los lenguajes de programación.
