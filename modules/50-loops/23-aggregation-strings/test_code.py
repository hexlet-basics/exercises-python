import index


def test1():
    assert index.join_numbers_from_range(2, 2) == '2'
    assert index.join_numbers_from_range(1, 5) == '12345'
    assert index.join_numbers_from_range(10, 12) == '101112'
