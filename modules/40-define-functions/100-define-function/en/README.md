
It is easier to write and maintain programs if you define your own functions. They allow you to combine compound operations into one. So in this lesson, we'll talk about how to create your own functions.

Let's say we want to send emails on a website. This is quite a complicated process that involves interaction with external systems. But if you define a function, all the complexity can be hidden behind one simple function:

```python
# Hypothetical example
# Where the function comes from
from emails import send

email = 'support@hexlet.io'
title = 'Help'
body = 'I wrote a success story, how can I get a discount?'

# There's just one call, but it's got a lot of logic inside
send(email, title, body)
```

Internally, this call does a lot; it connects to the mail server, forms a valid request based on the message header and body, and then sends everything out without forgetting to close the connection.

Let's create our first function. Its task is to display a greeting:

```text
Hello, Hexlet!
```

```python
# Function definition
# Defining a function does not invoke or execute it
# We're only saying that this function now exists
def show_greeting():
  # Indent four spaces inside the body
  text = 'Hello, Hexlet!'
  print(text)

# Function call
show_greeting()  # => 'Hello, Hexlet!'
```

Unlike ordinary data, functions perform actions. Therefore, their names should be specified through verbs: “build something,” “draw something,” “open something”.

The information that's indented below the function name is called the **function body**. Any code can be entered within the body. It's like a small independent program, with whatever instructions you put in

The body is executed the moment the function is started. In this case, each function call launches the body independently of the other calls.

The body of the function can be empty. In that case, the keyword `pass` is used inside it:

```python
# Minimum function definition
def noop():
  pass

noop()
```

The term “create a function” has many synonyms, you can also implement a function, or define it. These can often be found when working the real world. By creating your own function, you can make complex operations and development easier.
