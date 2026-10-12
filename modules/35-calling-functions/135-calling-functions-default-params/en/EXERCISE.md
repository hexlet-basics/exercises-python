The code defines data about a car trip: the distance, the fuel consumption, the fuel price and the number of passengers. Fuel consumption is given in litres per 100 kilometres.

Calculate and print three values:

1. The volume of fuel in litres needed for the trip. Round it to one decimal place.
2. The total cost of the trip. Round it to two decimal places.
3. The cost of the trip for each passenger. Round it to a whole number by calling `round()` without the second argument.

Round the values only when printing them. Calculate the total cost from the unrounded fuel volume and the cost per passenger from the unrounded total cost.

Each value is printed on its own line.

```text
distance ──────┐
               ├──→ fuel ──────┐
fuel_consumption ──┘           ├──→ trip_cost ──────┐
                               │                    ├──→ per_person
fuel_price ────────────────────┘                    │
                                                    │
passengers ─────────────────────────────────────────┘
```
