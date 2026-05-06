Implement the function `amount_per_person()`. It takes the restaurant bill total, the number of people, and the tip percentage, and returns the amount each person pays. The result is rounded up — nobody should underpay.

Use the `math.ceil()` function from the `math` module for rounding.

```python
# Bill 300, 4 people, 20% tip — total 360, each pays 90
print(amount_per_person(300, 4, 20))  # => 90

# Bill 350, 3 people, 10% tip — total 385, each pays 129
print(amount_per_person(350, 3, 10))  # => 129
```

## Hint

* First calculate the total with tip, then divide by the number of people and round up
* Don't forget to import the `math` module at the top of the file
