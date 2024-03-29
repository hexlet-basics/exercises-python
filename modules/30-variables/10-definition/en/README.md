
Imagine that we need to print the phrase _Father!_ on the screen twice. This can be done like so

```python
print('Father!')
print('Father!')
```

In the simplest case, that's what you should do. But if the phrase _Father!_ is used more than twice, or even in different parts of the program, you have to repeat it everywhere; it's a little inconvenient. The problems with this approach will begin when you need to change the phrase, and this happens quite often. We'll have to find all the places this phrase is located and make the required changes lots of times.

There is one other way to do it. In order not to copy the expression, you just need to create a variable with it.

```python
# greeting - translates as greeting
greeting = 'Father!'
print(greeting)
print(greeting)
# => Father!
# => Father!
```

In the line `greeting = 'Father!'` we take a variable named `greeting` and assign it the value `'Father!'` The variable points to the data that was written to it. In this way, the data can be used repeatedly and not be duplicated constantly.

Once you've created the variable, you can use it. You put it in the places where we originally had our phrase written out in full. When the code runs, the interpreter reaches the line `print(greeting)`, substitutes the contents of the variable, and then executes the code.

Any set of valid characters can be used for the variable name, which includes letters of the English alphabet, numbers and the `_` sign. Note that you can't place a digit at the beginning of a name. Variable names are case-sensitive, i.e., the name `hello` and the name `HELLO` are two different names for two different variables. Case is important in Python, never forget it.

The number of variables you can create is unlimited. Large programs contain tens or hundreds of thousands of variable names. This is what two variables look like inside one program:

```python
greeting1 = 'Father!'
print(greeting1)
print(greeting1)

greeting2 = 'Mother!'
print(greeting2)
print(greeting2)
```

To make the program easy to read, it's customary among programmers to create variables as close as possible to where they are used. Now we have to figure out how to change them.
