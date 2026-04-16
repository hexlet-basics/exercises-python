Learning a new programming language traditionally begins with 'Hello, World!'. It is a simple program that displays a greeting on the screen and introduces the new language — its syntax and structure.

```text
Hello, World!
```

This tradition is over forty years old, so we're keeping it. In the first lesson, we'll write a program called `Hello, World!`. In Python, the command for displaying text is `print()`:

```python
print('Hello, World!')
```

The way `print()` works: you put the text you want to display inside the parentheses. To let Python know it's text and not something else, wrap it in quotes. Both single and double quotes work — just make sure the opening and closing quote match:

```python
print('Hello, World!')
print("Hello, World!")
```

According to the Python style guide (PEP 8), single quotes are preferred for strings when there's no apostrophe inside.

```text
  Code             Interpreter          Screen
  ┌──────────┐     ┌─────────────┐     ┌──────────────┐
  │ print(…) │ ──→ │   Python    │ ──→ │ Hello, World!│
  └──────────┘     └─────────────┘     └──────────────┘
```

## Every character matters

Programming is not just English text. Code consists of commands, and each command must be written in a specific form. Besides letters, the code uses special characters: quotes `'` and `"`, parentheses `()`, comma `,`, exclamation mark `!`. Each character has its own role. Skip one or use the wrong one, and the program won't run.

Case matters too. If regular text treats `Hello` and `hello` as the same word, Python treats them as different. So `print`, `Print`, and `PRINT` are three different things — and only the first one works.

## Practice

Learning to code works best when you try things out as you read. You can run Python code line by line in an interactive environment (REPL) — [open it here](https://pyodide.org/en/stable/console.html) and experiment as you go through the lesson.
