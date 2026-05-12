import solution


def test():
    assert solution.amount_per_person(300, 4, 0) == 75
    assert solution.amount_per_person(300, 4, 20) == 90
    assert solution.amount_per_person(350, 3, 10) == 129
    assert solution.amount_per_person(100, 3, 0) == 34
