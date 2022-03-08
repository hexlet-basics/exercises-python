import index
from hexlet.test import expect_output


def test(capsys):
    index.print_reversed_word_by_symbol('Hexlet')
    expected = 't\ne\nl\nx\ne\nH'
    expect_output(capsys, expected)
