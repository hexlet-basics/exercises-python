
The `random()` function returns a random number from 0 to 1 with many decimal places. Implement code that displays a random integer between 0 and 10. For this task, you need the `random()` function and the [round()](https://docs.python.org/3/library/functions.html#round), function, which rounds the value passed to it

```python
round(2.320000789855705) # 2
```

Try to solve this task using only 1 line

## Algorithm
Since `random()` returns numbers between 0 and 1, we need to multiply by 10 to get numbers between 0 and 10. Then we round the result to get what we need.
