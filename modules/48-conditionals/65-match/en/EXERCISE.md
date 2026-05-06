
Implement the function `calculate_delivery_cost()`, which takes a delivery country and package weight in kilograms. The function should return the delivery cost.

Each country has two rates: one for packages up to and including 1 kg, and one for heavier packages:

* `'canada'`: 600 for packages up to 1 kg, 900 for the rest
* `'usa'`: 800 for packages up to 1 kg, 1200 for the rest
* `'germany'`: 700 for packages up to 1 kg, 1000 for the rest

If the country is unknown, the function should return `None`.

Function call examples:

```python
calculate_delivery_cost('canada', 0.5)  # 600
calculate_delivery_cost('canada', 2)    # 900
calculate_delivery_cost('usa', 1)       # 800
calculate_delivery_cost('france', 1)    # None
```
