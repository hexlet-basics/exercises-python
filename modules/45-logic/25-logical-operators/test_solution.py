import solution


def test1():
    assert solution.is_leap_year(2016)
    assert solution.is_leap_year(2000)
    assert not solution.is_leap_year(2017)
    assert not solution.is_leap_year(2018)
    assert not solution.is_leap_year(1900)
