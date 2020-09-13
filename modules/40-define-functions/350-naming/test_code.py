import importlib


def test():
    m = importlib.import_module('index')
    expected1 = '01-01-2001'
    assert m.get_formatted_birthday(1, 1, 2001) == expected1

    expected2 = '03-12-1999'
    assert m.get_formatted_birthday(3, 12, 1999) == expected2
