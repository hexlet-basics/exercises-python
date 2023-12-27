
Implement a method `is_leap_year()` that determines whether a year is a leap year or not. A year will be a leap year if it is a multiple of 400 (i.e. divisible without a remainder), or if it is both a multiple of 4 and not a multiple of 100. As you can see, the definition already contains all the necessary logic, all we need to do is to translate it into code:

```python
is_leap_year(2018) # false
is_leap_year(2017) # false
is_leap_year(2016) # true
```

The multiplicity can be checked as follows:

```python
# % - returns the remainder of the left operand divided by the right operand
# Check that the number is a multiple of 10
number % 10 == 0

# Check that the number is not a multiple of 10
number % 10 != 0
```
