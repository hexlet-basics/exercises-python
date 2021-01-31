import index


def test1(capsys):
    assert index.does_contain('Renly', 'R')
    assert not index.does_contain('Renly', 'r')
    assert index.does_contain('Tommy', 'm')
    assert not index.does_contain('Tommy', 'd')
    assert index.does_contain('Tommy', 'y')
