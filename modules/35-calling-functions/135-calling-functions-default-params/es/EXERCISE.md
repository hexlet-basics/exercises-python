En el código se han definido datos sobre un viaje en automóvil: la distancia, el consumo de combustible, el precio del combustible y la cantidad de pasajeros. El consumo de combustible se expresa en litros por cada 100 kilómetros.

Calcula y muestra en pantalla tres valores:

1. El volumen de combustible en litros necesario para el viaje. Redondéalo a un decimal.
2. El costo total del viaje. Redondéalo a dos decimales.
3. El costo del viaje para cada pasajero. Redondéalo al número entero, llamando a `round()` sin el segundo argumento.

Redondea los valores solo al mostrarlos. Calcula el costo total con el volumen de combustible sin redondear y el costo por pasajero con el costo total sin redondear.

Cada valor se muestra en una línea aparte.

```text
distance ──────┐
               ├──→ fuel ──────┐
fuel_consumption ──┘           ├──→ trip_cost ──────┐
                               │                    ├──→ per_person
fuel_price ────────────────────┘                    │
                                                    │
passengers ─────────────────────────────────────────┘
```
