import index


def test1():
    assert index.string_or_not("Hexlet") == "yes"
    assert index.string_or_not(10) == "no"
    assert index.string_or_not("") == "yes"
    assert index.string_or_not(False) == "no"
    assert index.string_or_not(True) == "no"
