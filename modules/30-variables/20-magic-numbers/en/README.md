
Let's look at our example of the program that calculates exchange rates:

```python
euros_count = 1000
dollars_count = euros_count * 1.25  # 1250.0
rubles_count = dollars_count * 60   # 75000.0

print(rubles_count)
```

From professional development's perspective, such code doesn't correspond with the best practices.

In this example, it's difficult to understand what the numbers `60` and `1.25` mean. Imagine having to deal with that code a month or a year from now – it's going to be difficult. It'll also be difficult for a programmer who hasn't seen the code before.

In our example, the context is easy to put together because the variables are named correctly. But in real projects, code is much more complicated, so it's often impossible to guess the meaning of the numbers.

The problem lies in magic numbers. These are numbers whose origin is impossible to understand at a glance – you have to dig deep into what's going on in the code.

To prevent this problem, you need to create variables with the right names. That way, everything will fall into place:

```python
dollars_per_euro = 1.25
rubles_per_dollar = 60

euros_count = 1000
dollars_count = euros_count * dollars_per_euro     # 1250.0
rubles_count = dollars_count * rubles_per_dollar  # 75000.0

print(rubles_count)
```

In this program:

* Snake_case naming is used
* The two new variables are separated from the subsequent calculations by a blank line. These variables make sense without calculations, so this separation is appropriate because it increases readability
* The resulting code is well named and structured, but it's longer than the previous version. This is often the case, but this is fine because the code must be readable

Magic numbers and obscure variable names don't break the code, but make it less readable.

It's important to understand that in any case, the computer will carry out the calculation you give it. However, another programmer reading the code won't understand, thus complicating your work. Naming the variables properly is half the battle when it comes to code analysis.
