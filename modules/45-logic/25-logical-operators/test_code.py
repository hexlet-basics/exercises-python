import index


def test1():
    assert index.is_leap_year(2016)
    assert index.is_leap_year(2000)
    assert not index.is_leap_year(2017)
    assert not index.is_leap_year(2018)
    assert not index.is_leap_year(1900)
