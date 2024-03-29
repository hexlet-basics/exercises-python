
The `is_infant()` function is a **predicate** or question function. A predicate answers a “yes or no” question by returning a boolean value Predicates usually have handy names in every language to make them easy to analyze. In Python, predicates begin with the prefix `is`, `are`, or `has`:

* `is_infant()` — "is it a baby?"
* `has_children()` — "are there children?"
* `is_empty()` — "is it empty?"
* `has_errors()` — "are there mistakes?"

A function is considered a predicate if it returns the boolean values `True` or `False`.

Let's write another predicate function. It takes a string and checks if it is the word `'Castle'`:

```python
def is_castle(string):
    return string == 'Castle'

print(is_castle('Sea')) # False
```
