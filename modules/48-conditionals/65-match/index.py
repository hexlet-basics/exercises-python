def get_currency_symbol(currency: str) -> str:
    match currency:
        case "USD":
            return "$"
        case "EUR":
            return "€"
        case "RUB":
            return "₽"
        case _:
            return "?"
