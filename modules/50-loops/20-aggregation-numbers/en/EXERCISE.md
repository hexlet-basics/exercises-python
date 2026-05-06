
Implement the function `calculate_electricity_bill()`, which takes the number of used kilowatt-hours and returns the electricity bill amount.

This exercise uses a tiered tariff. The first `100` kWh cost `5` each, the next `100` kWh cost `7` each, and every kWh above `200` costs `10`.

Go through the consumption with a loop and gradually accumulate the total amount.

```python
calculate_electricity_bill(80)   # 400
calculate_electricity_bill(150)  # 850
calculate_electricity_bill(250)  # 1700
```
