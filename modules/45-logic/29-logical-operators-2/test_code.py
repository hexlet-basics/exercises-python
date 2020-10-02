import index

def test1():
    assert index.is_neutral_soldier('yellow', 'black') == True
    assert index.is_neutral_soldier('red', 'yellow') == False
    assert index.is_neutral_soldier('red', 'red') == False
    assert index.is_neutral_soldier('black', 'black') == True
