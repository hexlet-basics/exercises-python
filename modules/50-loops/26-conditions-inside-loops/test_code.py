import index


def test1():
    assert index.count_chars('axe', 'a') == 1
    assert index.count_chars('', 'a') == 0
    assert index.count_chars('opPa', 'p') == 2
    assert index.count_chars('opPa', 'P') == 2
