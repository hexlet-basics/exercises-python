
Imagine that we need to change a character in a string. This is what will come out of it:

```python
first_name = 'Alexander'
first_name[0] = 'B'
# Error: TypeError: 'str' object does not support item assignment
```

This happens because of the immutability of primitive types in Python - the language does not give any physical possibility to change the string. The immutability of primitive types is important for many reasons. The key reason is performance.

But sometimes we need to change a string. That's what variables are for:

```python
first_name = 'Alexander'
first_name = 'Blexander'
print(first_name)  # => Blexander
```

There is a big difference between *changing the value of a variable* and *changing the value itself*. You can't change primitive types in Python, but you can change composite types. You can also change the value of a variable without any problem.
