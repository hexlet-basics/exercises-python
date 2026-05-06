Even experienced developers rarely get their code working perfectly on the first try. But the more experienced the developer, the better they are at **debugging** — analyzing errors and fixing them.

Debugging skills don't appear on their own — they must be developed, and the sooner you start, the better. During your studies you'll complete assignments and practice, which will help you gain experience. Over time, analyzing and fixing errors will become a habit if you devote enough attention to practice.

## How to find a bug in code

You can debug incorrectly working code by trial and error, but this is slow and unproductive. It will be much easier if you first understand the problem, and only then start fixing it. Understanding is the key step — without it, the next steps are impossible.

Before debugging code, you need to understand what's wrong with it. This can be done in two steps.

Step 1. Study the **traceback** — a list of all function calls from when the program started to the point where the error occurred. The traceback helps trace how the program executed: which functions were called successfully and which caused problems. Each entry in the traceback points to a file and line number, then to the function being executed.

Imagine you wrote code in a file `users.py` and called the function `main()` on line 4. The traceback entry would look like this:

```bash
  File "users.py", line 4, in <module>
    main()
```

As you can see, it shows not just the file and line number, but also the module name. This makes it easy to determine where the problem occurred: in your code or in a library you're using but didn't write.

Step 2. When the traceback reaches the problematic location, it will show an **error message**. For example:

```bash
NameError: name 'create' is not defined
```

The message says: "The name `create` is not defined." This error usually happens due to a typo in the name — check that first.

Now let's look at how the traceback and error message appear together:

```bash
Traceback (most recent call last):
  File "users.py", line 4, in <module>
    main()
  File "users.py", line 2, in main
    create()
NameError: name 'create' is not defined
```

In the example above, we can see the whole chain of events: the program successfully handled `main()`, then moved to `create()` and encountered a naming error.

Besides NameError, Python has many other types of errors, which can be divided into three groups.

## Types of errors

The simplest errors are **syntax errors**. They are purely about incorrectly formatted code — for example, using the wrong type of quotation marks.

The output of such errors always contains `SyntaxError:`. To debug code in this case, you need to carefully look at the location of the error. Here a syntax error occurred because `'` was used instead of `"`:

```bash
Traceback (most recent call last):
  File "users.py", line 2
    print("Hello" + "world')
                           ^
SyntaxError: EOL while scanning string literal
```

The second major group is **programming errors**. For example:

- Calling a non-existent function
- Using an undeclared variable
- Passing incorrect arguments (e.g., arguments of the wrong type)

These errors are harder to fix than syntax errors. They usually occur when there was incorrect logic in an earlier call.

The last type is **logic errors**. These can be very difficult to fix because the program generally works, but gives incorrect results for certain values. In most cases, the problem lies in incorrect logic. For example, subtraction is performed instead of addition:

```python
# The function should calculate the sum of numbers, but calculates the difference:
def sum(a: int, b: int) -> int:
    return a - b


# With this call the error is not obvious, because
# both addition and subtraction give the same result
sum(4, 0)  # 4
```

## Debugging methods

There are many ways to debug programs, but they all share one common idea — **you need to analyze how variable values change as the code runs**.

Let's look at a concrete example. Below is a function that calculates the sum of numbers from `start` to `finish`. If `start` is three and `finish` is five, the program should calculate: `3 + 4 + 5`.

```python
def sum_of_series(start: int, finish: int) -> int:
    result = 0
    n = start
    while n < finish:
        result = result + n
        n = n + 1
    return result
```

There's a bug in this code. Looking at the function `sum_of_series()`, we can see there are two main variables: `n` and `result`. To find the bug, we need to see what values the variables take at each iteration.

There's a handy tool for tracking variable values during execution — **visual debuggers**. They are built into popular code editors and allow you to run the program step by step and see all changes. To learn more, search Google for "Python debuggers."

In the Hexlet environment there is no debugger, so a different approach is used — **print debugging**. The principle is the same as with a visual debugger. The difference is that regular screen output is used to display variable values. What is printed to the screen appears in the `OUTPUT` tab, which the editor automatically switches to during checks. Let's look at an example:

```python
def sum_of_series(start: int, finish: int) -> int:
    result = 0
    n = start
    while n < finish:
        print("new iteration !!!!")
        print(n)
        result = result + n
        n = n + 1
        print(result)
    return result


sum_of_series(3, 5)

# new iteration !!!!
# 3
# 3
# new iteration !!!!
# 4
# 7
```

Here we can see there is one fewer loop iteration than needed. For some reason, the addition for the last number (`finish`) is not performed. And indeed, looking at the definition, `n < finish` is used instead of `n <= finish`. So debugging helped find the bug — the `<` sign was used instead of `<=`.

Beginners often get upset about errors and start thinking they are inattentive. In reality, errors are nothing to worry about: experienced developers make them just as often as beginners. It's hard to learn to write perfect code, but you can develop debugging skills and build familiarity with common errors.

Beginners also think that an experienced developer can look at code and immediately understand what's wrong. Yes, experience brings pattern recognition, but it's not that simple. **If you want to ask an experienced developer for advice, it's better to show them the error message rather than the incorrectly working code itself.**
