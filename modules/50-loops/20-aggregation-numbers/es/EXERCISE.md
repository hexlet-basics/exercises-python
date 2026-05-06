
Implementa la función `calculate_electricity_bill()`, que recibe la cantidad de kilovatios-hora consumidos y devuelve el importe de la factura de electricidad.

En este ejercicio se usa una tarifa por tramos. Los primeros `100` kWh cuestan `5` cada uno, los siguientes `100` kWh cuestan `7` cada uno y cada kWh por encima de `200` cuesta `10`.

Recorre el consumo con un ciclo y acumula poco a poco el importe total.

```python
calculate_electricity_bill(80)   # 400
calculate_electricity_bill(150)  # 850
calculate_electricity_bill(250)  # 1700
```
