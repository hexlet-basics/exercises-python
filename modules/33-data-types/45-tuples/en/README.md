Besides primitive types, Python has composite data types that store multiple values at once. A university student is described by a name, age, and GPA. A film has a title, release year, and rating. These groups of values are natural to store together.

A tuple is simpler than any other composite type. It stores several values in a strictly defined order. Once created, it cannot be changed.

A tuple works well for data that always belongs together.

```python
student = ('Alice', 20, 4.8)       # name, age, GPA
film = ('Inception', 2010, 8.8)    # title, year, rating
```

## Creating a tuple

A tuple is written in parentheses with values separated by commas.

```python
point = (10, 20)
colors = ('red', 'green', 'blue')
mixed = (42, 'hello', 3.14)
```

A single-element tuple requires a trailing comma. Without it, Python treats the parentheses as grouping an expression.

```python
single = (42,)    # a tuple with one element
not_tuple = (42)  # just the number 42
```

The parentheses are optional. Python recognizes a tuple by the commas.

```python
point = 10, 20
print(type(point))  # => <class 'tuple'>
```

## Accessing elements

Tuple elements are numbered from zero. They are accessed by index.

```python
point = (10, 20)
print(point[0])  # => 10
print(point[1])  # => 20
```

## Tuples are immutable

A tuple cannot be modified after creation. Attempting to replace an element raises an error.

```python
point = (10, 20)
point[0] = 5  # TypeError: 'tuple' object does not support item assignment
```

Immutability is built into tuples deliberately. No matter where a tuple is passed, its data stays the same.

## Unpacking

Tuple elements can be assigned to multiple variables at once.

```python
point = (10, 20)
x, y = point

print(x)  # => 10
print(y)  # => 20
```

Python matches values to variables in order. The number of variables must equal the number of elements.
