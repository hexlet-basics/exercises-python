import index

def test1():
    assert index.is_falsy('') == True
    assert index.is_falsy('a') == False
    assert index.is_falsy(0) == True
    assert index.is_falsy(10) == False
