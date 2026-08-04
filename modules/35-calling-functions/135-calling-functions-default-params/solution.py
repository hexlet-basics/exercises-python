distance = 450        # distance, km
fuel_consumption = 8.4  # fuel consumption, l/100 km
fuel_price = 64.2     # fuel price per litre
passengers = 4        # number of passengers

# BEGIN
fuel = distance / 100 * fuel_consumption
print(round(fuel, 1))

trip_cost = fuel * fuel_price
print(round(trip_cost, 2))

per_person = trip_cost / passengers
print(round(per_person))
# END
