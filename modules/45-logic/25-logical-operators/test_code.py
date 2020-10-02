import index

def test1():
    assert index.is_lannister_soldier('blue', None) == False
    assert index.is_lannister_soldier('red', 'man') == False
    assert index.is_lannister_soldier('red', 'lion') == True
    assert index.is_lannister_soldier('blue', 'lion') == True
    assert index.is_lannister_soldier('red', None) == True
