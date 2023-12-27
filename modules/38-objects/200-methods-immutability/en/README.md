
Imagine we have this call:

```python
name = 'Tirion'
print(name.upper())  # => TIRION
# What will this call print on the screen?
print(name)  # => ?
```

Calling the `.upper()` method returns a new value with all letters converted to upper case, but it does not change the original string. So inside the variable will be the old value: `'Tyrion'`. This logic holds true for methods of all primitive types.

Instead of changing the value, you can **replace** it. This requires variables:

```python
name = 'Tirion'
name = name.upper()
print(name)  # => TIRION
```
