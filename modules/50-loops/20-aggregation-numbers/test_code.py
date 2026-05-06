import index


def test1():
    assert index.calculate_electricity_bill(0) == 0
    assert index.calculate_electricity_bill(80) == 400
    assert index.calculate_electricity_bill(100) == 500
    assert index.calculate_electricity_bill(150) == 850
    assert index.calculate_electricity_bill(250) == 1700
