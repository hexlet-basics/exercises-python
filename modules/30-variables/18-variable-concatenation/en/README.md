
Let's try using variables with concatenation. Nothing will change syntactically. We know how to concatenate two lines:

```python
what = "Kings" + "road"
print(what)  # => Kingsroad
```

So we're able to glue together a string and one variable in which a string is written:

```python
first = "Kings"
what = first + "road"

print(what)  # => Kingsroad
```

You can also concatenate two variables with strings in them:

```python
first = "Kings"
last = 'road'

what = first + last
print(what)  # => Kingsroad
```

Variables are an important tool in programming. They simplify complex calculations and thus make development easier. But to work successfully with variables, you must not only use them correctly, but also call them correctly. We'll talk about this in the next lesson.
