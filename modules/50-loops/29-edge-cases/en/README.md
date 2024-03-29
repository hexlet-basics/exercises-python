
The `my_substr()` function you implemented in the last lesson contains quite a few errors. It passed the test because it had no **edge cases**. The function worked with normal arguments. Now let's imagine we passed it these length options:

* `0`
* Negative number
* A number that exceeds the actual size of the string

The `my_substr()` function isn't designed for this. The code will run in different situations with different combinations of conditions and data. You can't be sure that the arguments passed to it will always be correct, so you have to consider all cases.

Edge cases are a common cause of logic errors in programs. There's always something that programmers forget to take into account. These errors often don't manifest themselves immediately and may not lead to visible problems for a long time.

The program may continue to work, but at some point someone might notice an error in the results. It can some time be a result of Python having dynamic typing.

As you gain more experience, you'll learn to deal with these errors.

Here's an extended version of the `my_substr()` function. It takes three arguments: a string, an index, and the length of the substring to be extracted. The function returns a substring of the specified length, starting from the index passed. Call examples:

```python
string = 'If I look back I am lost'
print(my_substr(string, 0, 1))  # => 'I'
print(my_substr(string, 3, 6))  # => 'I look'
```

What **edge cases** to consider:

* If the extracted substring has a negative length
* The index given is negative
* The index given exceeds the boundary of the entire string
* The substring length together with the given index exceeds the boundary of the whole string

When the function is implemented, each edge case will be a separate piece of code. It'll most likely be implemented with `if`.

If you want to write `my_substr()` in a way that's protected against these cases, it's worth implementing a separate function that the arguments are valid
