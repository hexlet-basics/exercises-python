import index

def test1(capsys):
    assert index.does_contain('Renly', 'R') == True
    assert index.does_contain('Renly', 'r') == False
    assert index.does_contain('Tommy', 'm') == True
    assert index.does_contain('Tommy', 'd') == False
