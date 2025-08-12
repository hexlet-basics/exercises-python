
Imagine that we need to define a string that consists of several lines - that is, there are string translations `\n` inside. For example, it would look like this:

```python
text = 'Example of a text,\nconsisting of\nfew lines'
```

The line will look very different in print:

```bash
Example text,
consisting of
several lines
```

For such situations Python has another way of creating strings called **multi-line strings**. To describe such a «multi-line string», you need to put it in triple quotes — `"""` or `'''`. Inside the multi-line you can transfer the text and not use a line break `\n`:

```python
text = '''  Example text,
consisting of
several lines
'''
```

```bash
Example text,
consisting of
several lines

```

Notice that there is a blank line at the end of the text. It appears in the text because we put closing quotes `'''` on a new line. If you don't move the closing quotation marks to a new line, there will be no empty line in the text:

```python
text = '''  Example text,
consisting of
several lines'''
```

```bash
Example text,
consisting of
several lines
```

Because of the triple quotes, multi-line strings allow you not to escape quotes within a string:

```bash
There is no need to escape the 'single' and 'double' quotes
```

Even multi-line strings can become f-string for interpolation:

```python
a = 'A'
b = 'B'

# On the left was added f
text = f'''{a} и {b}
sitting on a pipe
'''
```

```text
А and B
sitting on a pipe

```

The computer doesn't care what kind of linking and line feeds you use. It will still do the calculations and give you the result you want. Interpolation and multi-line strings are used to make it easier for developers to read code.
