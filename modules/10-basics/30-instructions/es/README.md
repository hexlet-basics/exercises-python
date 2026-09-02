Al comando `print('Hexlet')` podemos llamarlo instrucción: le dice al intérprete de Python qué hay que hacer. Esas instrucciones pueden ser tantas como se quiera. Cada una se ejecuta después de que ha terminado la anterior, y así, a partir de elementos simples, obtenemos un programa tan grande y complejo como queramos.

```text
Instrucción 1: print('Hello')   →  ejecutada
        ↓
Instrucción 2: print('World')   →  ejecutada
        ↓
Instrucción 3: print('!')       →  ejecutada
```

Aquí tienes un ejemplo de código con dos instrucciones. Estas líneas le dicen al ordenador que muestre las frases en la pantalla.

```python
print("Mother of Dragons.")  # Primera instrucción
print("Dracarys!")  # Segunda instrucción
```

El resultado de la ejecución:

```text
Mother of Dragons.
Dracarys!
```

## El orden importa

El intérprete de Python ejecuta el código estrictamente en el orden en que lo escribiste. Si se intercambian las líneas:

```python
print("Dracarys!")
print("Mother of Dragons.")
```

en la pantalla también se intercambiarán:

```text
Dracarys!
Mother of Dragons.
```

## Forma alternativa de escritura

Normalmente las instrucciones se escriben en líneas separadas, pero Python permite unir varias instrucciones en una línea mediante `;`:

<!-- NOTE: форма записи и есть предмет урока. text чтобы форматтер не разбил строку -->

```text
print("Mother of Dragons."); print("Dracarys!")
```

Las dos versiones funcionan igual, pero la segunda variante es más difícil de leer. Por eso las instrucciones casi siempre se escriben una por línea.

## Para qué hace falta esto

Ahora escribimos programas muy simples, pero con el tiempo empezarán a complicarse, y una de las habilidades más importantes que ayudará a entenderlos es la capacidad de dividir (mentalmente) el programa en instrucciones independientes. Solo así se puede entender qué ocurre en el código. Abajo hay un ejemplo para llamar la atención; entenderlo por ahora no hace falta:

```python
def is_prime(number: int) -> bool:
    if number < 2:
        return False

    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            return False

        divider += 1

    return True
```
