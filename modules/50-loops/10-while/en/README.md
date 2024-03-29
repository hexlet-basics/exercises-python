
The programs we're writing in this course are becoming more complex and more extensive. They're still a long way from real programs, but we're not making it easy for you.

In this lesson, we'll be moving on to one of the most difficult of the basic topics in programming: **loops**.

Applications can help manage employees, control your finances, and provide entertainment. Despite their differences, they all execute the algorithms embedded in them, which bear a lot of similarities. An **algorithm** is a sequence of actions that leads to an expected result.

Let's imagine we have a book and we want to find a specific phrase in it. We remember the phrase itself, but we don't know what page it is on. We'll have to go through the pages one by one until we find the right one. This process is an example of an algorithm.

This algorithm includes logical checks and page lookups. The number of pages you'll have to look at isn't known to us in advance. But the viewing process itself is repeated in the same way. To perform repetitive actions, you need loops. Each repetition is called an **iteration**.

Let's write a function with a simple loop that will display the string `'Hello!'` `n` times:

```python
def print_hello(n):
  counter = 0
  while counter < n:
      print('Hello!')
      counter = counter + 1

print_hello(2)
# => Hello!
# => Hello!
```

Now let's analyze an example function with a loop that displays numbers from one to `n`, where `n` is passed to the funciton as an argument:

```python
print_numbers(3)
# => 1
# => 2
# => 3
```

You can't implement this function with the tools you've already learned, because we don't know the number of outputs in advance. But this isn't a problem for loops:

```python
def print_numbers(last_number):
  # i is short for index (ordinal number)
  # this is a generally agreed way of expressing the iteration number
  # as a loop counter
  i = 1
  while i <= last_number:
      print(i)
      i = i + 1
  print('finished!')

print_numbers(3)
# => 1
# => 2
# => 3
# => finished!
```

A `while' loop consists of three elements:

* The keyword `while'
* Predicate - a condition that comes after `while` and is calculated at each iteration
* Code block - loop body

Each execution of the body is called an **iteration**. In the example above, `print_numbers(3)` called three iterations, each one displaying the variable `i`. What we're basically saying is this: “do what's specified in the body of the loop as long as the condition `i <= last_number` is true”.

Let's look at how this code works when you call `print_numbers(3)`:

```python
# i is initialised
i = 1

# The predicate returns true, so the body of the loop is executed
while 1 <= 3
# print(1)
# i = 1 + 1

# The loop body has ended, so it goes back to the beginning
while 2 <= 3
# print(2)
# i = 2 + 1

# The loop body has ended, so it goes back to the beginning
while 3 <= 3
# print(3)
# i = 3 + 1

# The predicate returns false, so the loop is executed again
while 4 <= 3

# print('finished!');
# At this point, i is equal to 4, but we don't need it anymore
# Function ends
```

You need to make sure that the process that generates the loop is stopped.

Usually, the problem comes down to introducing a variable - **cycle counter**. First, it's initialized - an initial value is given to it. In our example, it's the line `i = 1`. The loop condition then checks if the counter hasn't reached its limit value.

The limit value in the example is determined by the argument of the function. If the loop condition isn't met, the body won't be executed and the interpreter will move on and start working with the instructions after the loop.

If the loop condition is true, the body in which the stop element is located will be executed. In this case, it's the changing of the counter. It's usually done at the end of the body, and you can't have the counter change without a variable. In the example above, the line `i = i + 1` is responsible for the change.

At this point, beginners make a lot of mistakes. For example, you may forget to increment the counter or check it incorrectly in the predicate. This will cause the loop to run indefinitely and the program will never stop. In this case, you need to force it to stop.

```python
def print_numbers(last_number):
  i = 1
  # This loop will never stop
  # and will always print the same value
  while i <= last_number:
      print(i)
  print('finished!')
```

In some cases, infinite loops are useful. We won't look at these situations right now, but we can show you what this code looks like:

```python
while True:
  # Doing something
```

You can't do without loops when an algorithm for completing a task requires actions to be repeated and we don't know how many times these actions need to be repeated.
