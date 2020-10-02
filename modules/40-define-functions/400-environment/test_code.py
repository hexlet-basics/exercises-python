import index


def test1():
    actual1 = index.get_age_difference(2001, 2018)
    assert actual1 == 'The age difference is 17'

    actual2 = index.get_age_difference(2020, 2010)
    assert actual2 == 'The age difference is 10'

    actual3 = index.get_age_difference(1980, 1980)
    assert actual3 == 'The age difference is 0'
