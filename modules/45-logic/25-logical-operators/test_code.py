import index


def test1():
    assert not index.is_lannister_soldier('blue', None)
    assert not index.is_lannister_soldier('red', 'man')
    assert index.is_lannister_soldier('red', 'lion')
    assert index.is_lannister_soldier('blue', 'lion')
    assert index.is_lannister_soldier('red', None)
