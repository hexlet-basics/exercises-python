If a Python program is written with a syntax violation, the interpreter stops and displays an error message. The message tells you the type of error, the file and line where it occurred, and often marks the exact spot where the interpreter got stuck.

## What is a syntax error?

A syntax error (SyntaxError) happens when code breaks the grammatical rules of the language: an unclosed string, a missing parenthesis, characters in the wrong order, and so on.

```text
  Code with error        Interpreter           Result
  ┌──────────────┐      ┌─────────────┐      ┌──────────────────┐
  │ print('Hi'   │  ──→ │   Python    │  ──→ │ SyntaxError:     │
  └──────────────┘      └─────────────┘      │ unexpected EOF   │
                                             └──────────────────┘
```

In natural languages, text with errors can usually be understood from context. In programming, the rules are strict: even a tiny violation makes the code impossible to run. Here is a simple example:

```python
print('Hodor)
```

The closing quote is missing. Running this produces:

```bash
$ python index.py
File "index.py", line 1
  print('Hodor)
              ^
SyntaxError: EOL while scanning string literal
```

The error message may look unfamiliar at first, but that's fine — the more you encounter these messages, the faster you'll understand them at a glance.

## Why syntax errors are considered easy

Syntax errors are tied to the rules of writing code rather than to its meaning, so they're straightforward to fix: find the violation and correct it. Many editors highlight syntax errors in real time, making them even easier to spot.

There is one nuance though: the interpreter doesn't always point to the exact location of the error. Sometimes the problem is a few lines above where the message appears. For example, an unclosed parenthesis on one line can "break" everything that follows.

## What to do when you see a syntax error

- Read the error message — it almost always contains useful information.
- Check the line the message points to.
- Check the line above it — the error is sometimes hidden there.
- Use an editor with syntax highlighting, like [VS Code](https://code.visualstudio.com/) — it helps catch unclosed quotes and brackets immediately.
