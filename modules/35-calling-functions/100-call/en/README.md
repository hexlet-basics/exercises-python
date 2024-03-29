
Addition, concatenation, finding the remainder of a division, and the other operations discussed are basic features of programming languages. Mathematics is not limited to arithmetic, there are other sections with their own operations ⎯ e.g., geometry. The same goes for strings: you can flip them, change a letter's case, delete extra characters – and that's just the tip of the iceberg.

And at higher levels, there's application-specific logic. Programs withdraw money, calculate taxes, and generate reports. The number of these operations is endless and different for each program. And you have to be able to express them in code.

For expressing other operations, we have a feature in programming called **functions**. Functions can be built-in or added by the programmer. We're already familiar with one built-in function ⎯  `print()`.

Functions are one of the key constructs in programming. Without them, it's impossible to do almost anything. It's important to get to know them as early as possible, since everything after this is going to be very function-heavy. First we'll learn how to use the functions we've already created, and then we'll learn how to create our own.

We'll start with basic functions that handle strings.

The `len()` function counts the number of characters in a string. Below is an example of it being called:

```python
# Calling the function len with the parameter 'Hello!
result = len('Hello!')
print(result)  # => 6
```

**Parameters or arguments** are the information the function receives when it is called. Based on this information, the function usually calculates and outputs a result.

We created a variable called `result` and gave the interpreter a specific action: we have to write into it the result returned by the `len()` function when it's called. In this sense, functions are like operations - they always return the result of their work. The entry `len('Hello!')` means that a function named *len* is called, to which the parameter `'Hello!'` is passed. The `len()` function counts the length of the string that was passed to it.

A function call is always indicated by parentheses `()`, which come immediately after the function name. There can be any number of parameters in brackets, and sometimes none at all. The number of parameters depends on the function used.

Take for example the `pow()` function, which increments a given number to the correct power. It takes two parameters as input: the first parameter is expanded by the degree set in the second parameter:

```python
result = pow(2, 3)  # 2 * 2 * 2
print(result)  # => 8
```

We've figured out how to use the simple built-in functions. But that's not all of them. You'll learn more about functions in future lessons
