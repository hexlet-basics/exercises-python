import solution


def test1():
    assert not solution.is_international_phone("89602223423")
    assert solution.is_international_phone("+79602223423")
