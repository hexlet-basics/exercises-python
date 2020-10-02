import index


def test1():
    assert index.is_not_lannister_soldier('blue', None)
    assert index.is_not_lannister_soldier('red', 'man')
    assert not index.is_not_lannister_soldier('red', 'lion')
    assert not index.is_not_lannister_soldier('blue', 'lion')
    assert not index.is_not_lannister_soldier('red', None)
