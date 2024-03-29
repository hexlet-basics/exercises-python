
Another type of task that needs loops is ones that involve **aggregating data**. These tasks include: finding the maximum or minimum value, finding the sum of something, or finding the mean. With these tasks, the result depends on the whole data set.

To calculate the sum, you have to add up all the numbers, and to calculate the maximum, you have to compare them. Accountants and marketers will be familiar with such tasks. They work in Microsoft Excel or Google Tables.

In this lesson, we'll look at how aggregation applies to numbers and strings.

Suppose we need to find the sum of a set of numbers. Let's implement a function that adds numbers in a specified range, including boundaries. A **range** is a set of numbers with an upper and lower limit. For example, the range [1, 10] includes the integers from one to ten.

Example:

```python
sum_numbers_from_range(5, 7)  # 5 + 6 + 7 = 18
sum_numbers_from_range(1, 2)  # 1 + 2 = 3

# [1, 1] - a range with the same beginning and end is also a range
# It includes one number, which is the range boundary itself
sum_numbers_from_range(1, 1)      # 1
sum_numbers_from_range(100, 100)  # 100
```

To implement this code, you need a loop, because adding numbers is an iterative process, i.e., it's repeated for every number. The number of iterations depends on the size of the range.

Check out the code below:

```python
def sum_numbers_from_range(start, finish):
    # It is technically possible to change the start
    # But the input arguments must be left at their original value
    # This will make the code easier to analyze
    i = start
    sum = 0  # Initializing the amount
    while i <= finish:  # Moving to the end of the range
        sum = sum + i   # Calculate the sum for each number
        i = i + 1       # Move to the next number in the range
    # Return the result
    return sum
```

The structure of the loop here is standard: there's a counter, which is initialized with the initial value of the range, a loop which has a condition requiring you to stop at the end of the range, and the counter changes at the end of the loop body. The number of iterations in such a loop is equal to `finish - start + 1`. For the range [5, 7], it's 7 - 5 + 1, which is three iterations.

The main difference from the usual way of processing is the logic of calculating the result. In aggregation tasks, there's always a variable that stores the result of the loop. In the code above, it's `sum`. It changes at each iteration of the loop: the next number in the range is added: `sum = sum + i`.

The process looks like this:

```python
# To call sum_numbers_from_range(2, 5)
sum = 0
sum = sum + 2  # 2
sum = sum + 3  # 5
sum = sum + 4  # 9
sum = sum + 5  # 14
# 14 is the result of adding numbers in the range [2, 5]
```

The `sum` variable has an initial value, any repeating operation will begin with it. In the example above, it's `0`.

In math, we have the concept of a **neutral element**, and each operation has a different one. An operation with this element doesn't change the value it's working on. For example, in addition, any number plus zero gives the number itself. It's the same for subtraction. Concatenation also has a neutral element, which is an empty string: `''` + `'one'` will be `'one'`.
