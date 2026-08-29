Implementa la función `get_traffic_light_action()`, que recibe el color de un semáforo y devuelve lo que debe hacer el conductor.

Las reglas:

* `'green'` → `'go'`
* `'yellow'` → `'slow down'`
* `'red'` → `'stop'`
* Cualquier otro color → `'unknown'`

Ejemplos de llamadas:

```python
print(get_traffic_light_action("green"))  # => 'go'
print(get_traffic_light_action("red"))  # => 'stop'
print(get_traffic_light_action("purple"))  # => 'unknown'
```
