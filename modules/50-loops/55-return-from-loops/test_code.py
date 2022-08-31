from index import is_contains_char


def test_is_contains_char():
    assert is_contains_char('Hexlet', 'H') == True
    assert is_contains_char('Hexlet', 'h') == False
    assert is_contains_char('Awesomeness', 'm') == True
    assert is_contains_char('Awesomeness', 'd') == False
    assert is_contains_char('Awesomeness', 'o') == True
