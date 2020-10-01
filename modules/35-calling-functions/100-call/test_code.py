import importlib
from hexlet.test import expect_output

def test(capsys):
    expected = '125'
    expect_output(capsys, expected)
