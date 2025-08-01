At the most basic level, computers only use numbers. Even in high-level language applications, there are many numbers and operations with them. But knowing basic arithmetic is enough for now, and that's where we'll start.

For example, to add two numbers in math, we write: `3 + 4`. The same goes for programming. Here's a program that adds up two numbers:

```python
3 + 4
```

Arithmetic in programming is virtually the same as in school arithmetic.

The code `3 + 4` will make the interpreter add the numbers and find the result. This program will work, but it makes no sense. In fact, we're not really giving the interpreter a command, we're just saying “oi, what's three plus four?” In real life, you need to do more than just tell the interpreter about the mathematical expression on its own.

For example, if you're creating an online store, you can't just ask the interpreter to calculate the cost of items in the shopping cart. You have to ask it to calculate the cost **И** show the price to the buyer.

We need to ask the interpreter to calculate `3 + 4` **AND** give it an order to do something with the result. For example, print it:

```python
# First, the amount is calculated,
# it's then passed to the print function
print(3 + 4)
```

After launching, the result will appear on the screen:

```text
7
```

In addition to addition, the following operations are available:

* `-` — subtraction
* `*` — multiplication
* `**` — exponentiation (e.g. 2 to the power of 4, 2^4)
* `/` — division
* `//` — [integer division](https://en.wikipedia.org/wiki/Euclidean_division)
* `%` — [modulus operation](https://en.wikipedia.org/wiki/Euclidean_division)

Now let's print the result of division and then the result of exponentiation:

```python
print(8 / 2)   # => 4.0 (Dividing two numbers produces the float data type)
print(3 ** 2)  # => 9
```

Sometimes, for convenience, we'll show in the result of running lines of code in the comments like this: `=> RESULT`. For example, `# => 4`.

The first instruction will display `4` (because 8 / 2 equals 4), and the second instruction will display 9 (because 3<sup>2</sup> equals 9).
