distance = 450        # расстояние, км
fuel_consumption = 8.4  # расход топлива, л/100 км
fuel_price = 64.2     # цена топлива, руб./литр
passengers = 4        # количество пассажиров

# BEGIN
fuel = distance / 100 * fuel_consumption
print(round(fuel, 1))

trip_cost = fuel * fuel_price
print(round(trip_cost, 2))

per_person = trip_cost / passengers
print(round(per_person))
# END
