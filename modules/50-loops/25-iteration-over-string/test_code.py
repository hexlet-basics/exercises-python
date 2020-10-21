import index
from hexlet.test import expect_output


def test(capsys):
    index.print_name_by_symbol('Hexlet')
    expected = 't\ne\nl\nx\ne\nH'
    expect_output(capsys, expected)
