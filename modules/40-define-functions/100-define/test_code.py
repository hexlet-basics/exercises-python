import index
from hexlet.test import expect_output


def test(capsys):
    index.print_motto()
    expected = 'Winter is coming'
    expect_output(capsys, expected)
