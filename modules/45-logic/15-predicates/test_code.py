import index

def test1():
    assert index.is_mister('8234782') == False
    assert index.is_mister('Joker') == False
    assert index.is_mister('Mister') == True
