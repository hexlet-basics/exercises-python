En Python, los valores de distintos tipos se pueden usar directamente en expresiones lógicas. Al hacerlo se comportan como `True` o `False`, según pertenezcan a la categoría **truthy** o **falsy**.

```python
if "hello":
    print("cadena no vacía — truthy")  # se ejecutará

if not 0:
    print("cero — falsy")  # se ejecutará
```

## Valores falsy y truthy

En Python hay un conjunto fijo de valores que se consideran **falsos** (`falsy`). A ellos pertenecen `0` y cualquier número nulo (`0.0`), la cadena vacía `""`, las colecciones vacías `[]`, `{}`, `set()`, `()` (todavía no las hemos visto) y también el valor especial `None`.

Todos los demás valores se consideran **verdaderos** (`truthy`). Son, por ejemplo, cualquier número distinto de cero (`1`, `-3.5`), una cadena no vacía (`"hi"`, `"0"`) y las colecciones no vacías (`[1]`, `{"a": 1}`, `(0,)`) (las estudiaremos en otros cursos de Hexlet).

## Cómo funcionan las expresiones lógicas

En Python las expresiones lógicas no devuelven solo `True` o `False`. Devuelven uno de sus operandos. El operador `and` devuelve el primer operando falsy o el último truthy. El operador `or` devuelve el primer operando truthy o el último falsy. Por eso el resultado puede ser una cadena, un número o cualquier otro objeto que participe en la expresión.

```python
# and devuelve el primer falsy o el último operando
print("hello" and "world")  # => "world"  (los dos truthy — el último)
print("" and "world")  # => ""       (el primer falsy)
print(0 and "world")  # => 0        (el primer falsy)

# or devuelve el primer truthy o el último operando
print("hello" or "world")  # => "hello"  (el primer truthy)
print("" or "world")  # => "world"  (el primer truthy)
print("" or 0)  # => 0        (los dos falsy — el último)
```

El orden de evaluación depende de la prioridad de los operadores.

```text
Prioridad (de la más alta a la más baja):

  ()          paréntesis
   ↓
  not         negación
   ↓
  and         Y lógico
   ↓
  or          O lógico
```

## Ejemplo con el resto de la división

```python
result = 10 % 2 == 0 and "yes" or "no"
print(result)  # => "yes"
```

Analicemos esa expresión paso a paso. Primero se ejecuta la aritmética `10 % 2 == 0` → `True`. Después actúa `and`: como a la izquierda hay verdad, el resultado pasa a ser `"yes"`. Como `"yes"` es truthy, el operador `or` devuelve precisamente ese valor.

El mismo principio dentro de una función:

```python
def parity(number: int) -> str:
    return number % 2 == 0 and "even" or "odd"


print(parity(10))  # => "even"
print(parity(7))  # => "odd"
```

## Ejemplos

```python
print(7 % 2 == 0 and "even" or "odd")
# => "odd"

print(("" and "not empty") or "empty")
# => "empty"

print(("hello" and "not empty") or "empty")
# => "not empty"

print((-5 > 0 and "positive") or "non-positive")
# => "non-positive"
```

## Uso en funciones

La particularidad de los valores truthy y falsy resulta cómoda de aplicar en las funciones. Por ejemplo, se puede escribir una función que devuelve un texto si no está vacío, o un valor por defecto si la cadena está vacía.

```python
def get_text_or_default(text: str, default: str = "empty") -> str:
    return text or default


print(get_text_or_default("hello"))  # => "hello"
print(get_text_or_default(""))  # => "empty"
```

Aquí la expresión `text or default` funciona así: si `text` no está vacío (truthy), la función lo devolverá. Si `text` está vacío (falsy), la función devolverá `default`.
