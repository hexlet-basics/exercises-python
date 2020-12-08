import index


def test1():
    text = 'If I look back I am lost'
    assert index.filter_string(text, 'w') == 'If I look back I am lost'
    assert index.filter_string(text, 'I') == 'f  look back  am lost'
    assert index.filter_string('zz zorro', 'z') == ' orro'
