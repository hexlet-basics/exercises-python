import index

def test1():
    assert index.has_targaryen_reference('') == False
    assert index.has_targaryen_reference('Targari') == False
    assert index.has_targaryen_reference('targaryen') == False
    assert index.has_targaryen_reference('Targaryens') == True
    assert index.has_targaryen_reference('Targaryen') == True
