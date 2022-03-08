import index


def test1():
    assert index.multiply_numbers_from_range(2, 2) == 2
    assert index.multiply_numbers_from_range(1, 3) == 6
    assert index.multiply_numbers_from_range(1, 5) == 120
