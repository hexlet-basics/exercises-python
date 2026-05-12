import solution


def test1():
    assert not solution.is_pensioner(23)
    assert solution.is_pensioner(70)
    assert solution.is_pensioner(60)
    assert not solution.is_pensioner(59)
