from index import is_contains_char


def test_is_contains_char():
    assert is_contains_char('Hexlet', 'H') is True
    assert is_contains_char('Hexlet', 'h') is False
    assert is_contains_char('Awesomeness', 'm') is True
    assert is_contains_char('Awesomeness', 'd') is False
    assert is_contains_char('Awesomeness', 'o') is True
