import index


def test1():
    assert index.is_falsy('')
    assert not index.is_falsy('a')
    assert index.is_falsy(0)
    assert not index.is_falsy(10)
