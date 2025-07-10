from index import print_table_of_squares
from hexlet.test import expect_output


def test(capsys):
    expected = """square of 1 is 1
square of 2 is 4
square of 3 is 9
square of 4 is 16
square of 5 is 25
square of 6 is 36
square of 7 is 49
square of 8 is 64
square of 9 is 81
square of 10 is 100"""

    print_table_of_squares(1, 10)
    expect_output(capsys, expected)
