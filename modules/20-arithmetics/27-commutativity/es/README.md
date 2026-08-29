La frase «el orden de los sumandos no altera la suma» le resulta familiar a cualquiera desde la escuela. Ese principio se llama ley conmutativa y es una de las leyes básicas de la aritmética.

## Qué es la conmutatividad

Una operación se llama conmutativa si el orden de los operandos no influye en el resultado: intercambiando los valores obtendrás la misma respuesta. Un ejemplo de operación conmutativa: la suma.

```python
print(3 + 2)  # => 5
print(2 + 3)  # => 5
```

El resultado idéntico confirma que la operación es conmutativa.

```text
2 + 3 = 5     3 + 2 = 5
└──────────┬─────────┘
  mismo resultado

2 - 3 = -1    3 - 2 = 1
└──────────┬─────────┘
  resultado distinto
```

## Operaciones no conmutativas

Pero no todas las operaciones tienen esa propiedad. Por ejemplo, la resta es una operación no conmutativa:

```python
print(2 - 3)  # => -1
print(3 - 2)  # => 1
```

Intercambiar los operandos da otro resultado.

## En programación es exactamente igual

La conmutatividad en programación funciona exactamente igual que en aritmética. Python sigue estrictamente las reglas matemáticas.

Otras operaciones no conmutativas:

- La división: _8 / 2 ≠ 2 / 8_
- La potenciación: _2 **3 ≠ 3** 2_

Ejemplos en código:

```python
# División
print(8 / 2)  # 8 dividido entre 2 = 4.0

# Potenciación
print(3**2)  # 3 al cuadrado = 9
```

Por eso:

- Comprueba siempre con atención el orden de los operandos, especialmente al trabajar con operaciones desconocidas;
- comprueba la conmutatividad de forma experimental, en vez de suponerla de antemano.
