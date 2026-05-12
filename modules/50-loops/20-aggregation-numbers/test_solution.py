import solution


def test1():
    assert solution.calculate_electricity_bill(0) == 0
    assert solution.calculate_electricity_bill(80) == 400
    assert solution.calculate_electricity_bill(100) == 500
    assert solution.calculate_electricity_bill(150) == 850
    assert solution.calculate_electricity_bill(250) == 1700
