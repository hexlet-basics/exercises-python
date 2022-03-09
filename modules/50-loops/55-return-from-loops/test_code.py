import index


def test1(capsys):
    assert index.is_contains_char('Hexlet', 'H')
    assert not index.is_contains_char('Hexlet', 'h')
    assert index.is_contains_char('Awesomeness', 'm')
    assert not index.is_contains_char('Awesomeness', 'd')
    assert index.is_contains_char('Awesomeness', 'o')
