
Constructions like `index = index + 1` are often found in Python, so the creators of the language added an abbreviated version: `index += 1`.

The only difference is how they're written. The interpreter will turn an abbreviated construction into its expanded form.

These abbreviations are called **syntactic sugar** because they make the process of writing code a little easier and more pleasant.

This form is especially common in loops, where we often change a counter and accumulate a result:

```python
sum = 0
index = 1

while index <= 5:
    sum += index      # Same as sum = sum + index
    index += 1        # Same as index = index + 1

print(sum)  # => 15
```

Without abbreviated assignment, the loop body would be longer:

```python
while index <= 5:
    sum = sum + index
    index = index + 1
```

There are abbreviated forms for all arithmetic operations and for string concatenation:

* `a = a + 1` → `a += 1`
* `a = a - 1` → `a -= 1`
* `a = a * 2` → `a *= 2`
* `a = a / 1` → `a /= 1`
