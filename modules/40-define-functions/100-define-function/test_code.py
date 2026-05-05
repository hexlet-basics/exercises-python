import index
from hexlet.test import expect_output


def test(capsys):
    index.say_hello()
    expected = "Hello, World!"
    expect_output(capsys, expected)
