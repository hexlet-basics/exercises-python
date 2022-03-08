import index


def test1(capsys):
    assert index.does_contain('Hexlet', 'H')
    assert not index.does_contain('Hexlet', 'h')
    assert index.does_contain('Awesomeness', 'm')
    assert not index.does_contain('Awesomeness', 'd')
    assert index.does_contain('Awesomeness', 'o')
