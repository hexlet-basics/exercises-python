import index
from hexlet.test import expect_output


def test1(capsys):
    index.print_numbers(2)
    expect_output(capsys, '2\n1\nfinished!')


def test2(capsys):
    index.print_numbers(4)
    expect_output(capsys, '4\n3\n2\n1\nfinished!')
