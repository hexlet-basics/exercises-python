The code defines data about a car trip: the distance, the fuel consumption, the fuel price and the number of passengers.

Calculate and print three values:

1. The volume of fuel in litres needed for the trip. Round it to one decimal place.
2. The total cost of the trip. Round it to two decimal places.
3. The cost of the trip for each passenger. Round it to a whole number by calling `round()` without the second argument.

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
