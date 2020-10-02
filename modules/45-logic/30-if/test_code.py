import index


def test1():
    assert index.guess_number(100500) == 'Try again!'
    assert index.guess_number(42) == 'You win!'
