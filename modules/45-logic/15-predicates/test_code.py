import index


def test1():
    assert not index.is_mister('8234782')
    assert not index.is_mister('Joker')
    assert index.is_mister('Mister')
