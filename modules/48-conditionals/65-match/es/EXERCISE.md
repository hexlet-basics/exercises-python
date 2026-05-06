
Implementa la función `calculate_delivery_cost()`, que recibe el país de entrega y el peso del paquete en kilogramos. La función debe devolver el costo de entrega.

Cada país tiene dos tarifas: una para paquetes de hasta 1 kg incluido y otra para paquetes más pesados:

* `'canada'`: 600 para paquetes de hasta 1 kg, 900 para el resto
* `'usa'`: 800 para paquetes de hasta 1 kg, 1200 para el resto
* `'germany'`: 700 para paquetes de hasta 1 kg, 1000 para el resto

Si el país es desconocido, la función debe devolver `None`.

Ejemplos de llamadas a la función:

```python
calculate_delivery_cost('canada', 0.5)  # 600
calculate_delivery_cost('canada', 2)    # 900
calculate_delivery_cost('usa', 1)       # 800
calculate_delivery_cost('france', 1)    # None
```
