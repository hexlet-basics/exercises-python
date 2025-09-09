
Let's look at the `round()` function, which rounds the number passed to it:

```python
result = round(10.25, 0)  # 10.0
```

We passed two parameters to it:

* Number to be rounded
* Rounding accuracy

`0` means that the rounding will be to an integer value. More often than not, you need to round to a whole number, not to two, three, four etc. decimal places. So the creators of the `round` function made the second parameter **unnecessary** and gave it a **default value of `0`** inside the function. So, you can choose to not specify the second parameter and the result will be the same:

```python
result = round(10.25)  # 10.0
```

And if you need a different precision, you can pass a parameter:

```python
# rounding to one decimal place
result = round(10.25, 1)  # 10.2
```

If a function in Python accepts optional arguments, they always come after the mandatory ones. There can be any number of them. It depends on the function itself, but they always go next to and at the end of the list of arguments.
