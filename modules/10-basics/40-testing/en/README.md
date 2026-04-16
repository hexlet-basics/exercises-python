Our site automatically checks your solutions. Here is how it works.

In the simplest case, the system runs your code and looks at what appears on the screen, then compares it to what the task expected. For example, if the task is "display the number 10", your code might look like this:

```python
print(10)
```

The system runs it and checks that `10` actually appears on the screen. If it matches — the solution is accepted. If not, you'll see an error:

```bash
E   AssertionError: assert '9' == '10'
E
E     - 10
E     + 9
```

The line with `-` shows the value the test expected. The line with `+` shows what your code actually produced.

In later, more complex lessons, you will write functions — mini-programs that take input from the outside world and perform operations. Checking those solutions works a bit differently: the system calls your function with different inputs and compares the results against the correct answers. If all the answers match, the solution is accepted.

This approach is called testing, and it's used in real everyday development. Typically, a developer writes a test first — a checking program — and then writes the actual program. Along the way, they constantly run the tests to see how close they are to a working solution. That's why the site says "Tests passed" when you solve a problem correctly.

## My fault or not?

Sometimes it may seem like you've done everything right, but the system keeps rejecting the solution. In practice, this almost never happens because of a bug in the tests — tests are automatically run after every change and can't reach the site if they're broken. In the vast majority of cases, the mistake is in the solution code. It can be very subtle: a Russian letter typed instead of an English one, wrong letter case, a missing comma. Other cases are trickier — your solution might work for one set of inputs but fail for another.

Always read the task description and the test output carefully. There is almost always a clue pointing to the error.

If you're convinced there's a mistake in the task itself, you can report it. This project is open source on [GitHub](https://github.com/hexlet/code-basics), so you can open an issue, read the test code to see how your solution is called, or even send a pull request.
