import index


def test1():
    assert index.get_currency_symbol("USD") == "$"
    assert index.get_currency_symbol("EUR") == "€"
    assert index.get_currency_symbol("RUB") == "₽"
    assert index.get_currency_symbol("GBP") == "?"
    assert index.get_currency_symbol("JPY") == "?"
