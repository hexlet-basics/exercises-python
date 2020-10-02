import index

def test1():
    assert index.is_not_lannister_soldier('blue', None) == True
    assert index.is_not_lannister_soldier('red', 'man') == True
    assert index.is_not_lannister_soldier('red', 'lion') == False
    assert index.is_not_lannister_soldier('blue', 'lion') == False
    assert index.is_not_lannister_soldier('red', None) == False
