import solution


def test1():
    assert solution.string_or_not("Hexlet") == "yes"
    assert solution.string_or_not(10) == "no"
    assert solution.string_or_not("") == "yes"
    assert solution.string_or_not(False) == "no"
    assert solution.string_or_not(True) == "no"
