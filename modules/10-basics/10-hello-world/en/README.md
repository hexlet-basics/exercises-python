Learning a new programming language traditionally begins with 'Hello, World!'. It is a simple program that displays a greeting on the screen and introduces the new language — its syntax and structure.

```text
Hello, World!
```

This tradition is over forty years old, so we're keeping it. In the first lesson, we'll write a program called `Hello, World!`. In Python, the command for displaying text is `print()`:

```python
print("Hello, World!")
```

The way `print()` works: you put the text you want to display inside the parentheses. To let Python know it's text and not something else, wrap it in quotes. Both single and double quotes work — just make sure the opening and closing quote match:

<!-- NOTE: две формы записи кавычек и есть предмет урока. text чтобы форматтер не свёл их к одной форме -->

```text
print('Hello, World!')
print("Hello, World!")
```

The Python style guide (PEP 8) prefers neither single nor double quotes: pick one style and stick to it. This course uses double quotes. PEP 8 does advise picking the other kind when the string itself contains a quote — the apostrophe in `it's` breaks a single-quoted string, so that one needs double quotes.

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
