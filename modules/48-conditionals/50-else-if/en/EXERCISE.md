Implement the function `get_traffic_light_action()`, which takes a traffic light colour and returns what the driver has to do.

The rules:

- `'green'` → `'go'`
- `'yellow'` → `'slow down'`
- `'red'` → `'stop'`
- Any other colour → `'unknown'`

Example calls:

```python
print(get_traffic_light_action("green"))  # => 'go'
print(get_traffic_light_action("red"))  # => 'stop'
print(get_traffic_light_action("purple"))  # => 'unknown'
```
