def calculate_delivery_cost(country: str, weight: float) -> int | None:
    match country:
        case "canada":
            if weight <= 1:
                return 600
            return 900
        case "usa":
            if weight <= 1:
                return 800
            return 1200
        case "germany":
            if weight <= 1:
                return 700
            return 1000
        case _:
            return None
