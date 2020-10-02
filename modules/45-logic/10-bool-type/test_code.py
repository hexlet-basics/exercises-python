import index

def test1():
    assert index.is_pensioner(23) == False
    assert index.is_pensioner(70) == True
    assert index.is_pensioner(60) == True
    assert index.is_pensioner(59) == False
