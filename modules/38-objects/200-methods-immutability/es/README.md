
Supongamos que tenemos la siguiente ejecución:

```python
name = 'Tirion'
print(name.upper())  # => TIRION
# ¿Qué imprimirá esta ejecución?
print(name)  # => ?
```

La llamada al método `.upper()` devuelve un nuevo valor en el que todas las letras están convertidas a mayúsculas, pero no modifica la cadena original. Por lo tanto, el valor dentro de la variable seguirá siendo el antiguo: `'Tirion'`. Esta lógica se aplica a los métodos de todos los tipos primitivos.

En lugar de modificar los valores, se pueden **reemplazar** los valores. Para ello, se necesitan variables:

```python
name = 'Tirion'
name = name.upper()
print(name)  # => TIRION
```

https://replit.com/@hexlet/python-basics-objects-methods-immutability
