import index


def test1():
    assert index.is_neutral_soldier('yellow', 'black')
    assert not index.is_neutral_soldier('red', 'yellow')
    assert not index.is_neutral_soldier('red', 'red')
    assert not index.is_neutral_soldier('yellow', 'red')
    assert index.is_neutral_soldier('black', 'black')
