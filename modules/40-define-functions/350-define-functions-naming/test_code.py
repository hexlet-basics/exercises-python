import index


def test1():
    actual1 = index.get_formatted_birthday(1, 1, 2001)
    assert actual1 == '01-01-2001'

    actual2 = index.get_formatted_birthday(3, 12, 1999)
    assert actual2 == '03-12-1999'
