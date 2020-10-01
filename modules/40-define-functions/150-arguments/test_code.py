import index
from hexlet.test import expect_output

def test1(capsys):
    index.print_seq('0-', 5)
    expected = '0-0-0-0-0-'
    expect_output(capsys, expected)

def test2(capsys):
    index.print_seq('-1', 2)
    expected = '-1-1'
    expect_output(capsys, expected)
