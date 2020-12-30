from index import filter_string


def test1():
    text = 'If I look forward I am win'
    assert filter_string(text, 'z') == 'If I look forward I am win'
    assert filter_string(text, 'I') == 'f  look forward  am wn'
    assert filter_string('zz zorro', 'z') == ' orro'
