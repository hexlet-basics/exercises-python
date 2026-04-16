When we're making a dish, we follow the recipe carefully. Otherwise, the food won't turn out as expected. The same rule applies to programming.

If you want to see the expected result on screen, the computer needs clear, step-by-step directions. This is done using instructions. An instruction is a command to the computer — a unit of execution. Python code is a set of instructions, presented like a step-by-step recipe.

Python code is run by an **interpreter**, a program that executes instructions strictly, line by line. Like the steps in a recipe, the instructions for the interpreter are written in order and separated from each other by a line break.

```text
  Instruction 1: print('Hello')   →  executed
          ↓
  Instruction 2: print('World')   →  executed
          ↓
  Instruction 3: print('!')       →  executed
```

Here is an example of code with two instructions. When it runs, two lines appear on the screen one after another:

```python
print('Mother of Dragons.') # first instruction
print('Dracarys!') # second instruction
# => Mother of Dragons.
# => Dracarys!
```

## Order matters

The interpreter executes code in exactly the order you write it. Swap the lines, and the output changes too:

```python
print('Dracarys!')
print('Mother of Dragons.')
# => Dracarys!
# => Mother of Dragons.
```

Developers need to keep the order of operations in mind and be able to mentally divide a program into independent parts.

## Alternative syntax

Instructions are usually written on separate lines, but Python also allows multiple instructions on one line, separated by a semicolon `;`:

```python
print('Mother of Dragons.'); print('Dracarys!')
```

There is no technical difference between the two versions — the interpreter handles them the same way. But the second version is harder to read, so in real projects instructions are always written one per line.
