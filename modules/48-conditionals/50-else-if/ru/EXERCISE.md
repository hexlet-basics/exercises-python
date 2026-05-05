Реализуйте функцию `get_traffic_light_action()`, которая принимает цвет светофора и возвращает, что нужно делать водителю.

Правила:

* `'green'` → `'go'`
* `'yellow'` → `'slow down'`
* `'red'` → `'stop'`
* Любой другой цвет → `'unknown'`

Примеры вызова:

```python
print(get_traffic_light_action('green'))   # => 'go'
print(get_traffic_light_action('red'))     # => 'stop'
print(get_traffic_light_action('purple'))  # => 'unknown'
```
