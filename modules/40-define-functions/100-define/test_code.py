import index
from hexlet.test import expect_output

def test1(capsys):
    index.print_jaimes_line('hey')
    expected = 'JAIME: hey'
    expect_output(capsys, expected)

def test2(capsys):
    index.print_jaimes_line('Farewell, my friend...')
    expected = 'JAIME: Farewell, my friend...'
    expect_output(capsys, expected)
