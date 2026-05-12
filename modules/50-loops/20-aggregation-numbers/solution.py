def calculate_electricity_bill(kwh: int) -> int:
    total = 0
    current = 1
    while current <= kwh:
        if current <= 100:
            total += 5
        elif current <= 200:
            total += 7
        else:
            total += 10
        current += 1
    return total
