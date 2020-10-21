import index


def test1():
    string = 'If I look back I am lost'
    assert index.count_chars(string, 'I') == 3
    assert index.count_chars(string, 'z') == 0
    assert index.count_chars(string, 'o') == 3
    assert index.count_chars(string, 't') == 1
