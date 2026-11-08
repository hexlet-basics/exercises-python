A message can contain the characters `<`, `>` and `&`. When displayed on an HTML page, a browser can interpret them as markup. The standard-library package `html` replaces these characters with special sequences to preserve the message text.

## Task

Implement the function `escape_html(text)`. It takes a string and returns the result of the `escape()` function from the `html` package with its default arguments. Single and double quotes are also replaced.

```python
print(escape_html("<b>A & B</b>"))  # => &lt;b&gt;A &amp; B&lt;/b&gt;
print(escape_html('"Hello"'))  # => &quot;Hello&quot;
print(escape_html("It's ok"))  # => It&#x27;s ok
print(escape_html("Hello"))  # => Hello
```

## Hints

- `html` is a regular package in the standard library. Its _\_\_init\_\_.py_ file provides the `escape()` function
- Import the package with `import html` or the function with `from html import escape`
- [html.escape documentation](https://docs.python.org/3/library/html.html#html.escape)
