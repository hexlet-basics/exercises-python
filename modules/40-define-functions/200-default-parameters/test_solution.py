import solution


def test():
    assert solution.get_hidden_card("1234123412341234") == "****1234"
    assert solution.get_hidden_card("1234123412344321") == "****4321"
    assert solution.get_hidden_card("1234123412344321", 3) == "***4321"
