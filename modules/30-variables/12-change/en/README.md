
The word “variable” itself suggests that it can be changed. And indeed, the values of variables can change over time within the program.

For example:

```python
# greeting 
greeting = 'Father!'
print(greeting)  # => Father!

greeting = 'Mother!'
print(greeting)  # => Mother!
```

The name remained the same, but there were different data inside. Note that variables in Python require no special declaration. Instead, a variable is declared when it is first used in a program.

Variables are a powerful yet risky thing. You can't be sure right away what'll be inside it - first you have to analyze the code that comes before the variable. This is what developers do during debugging, when they try to figure out why the program doesn't work as intended.
