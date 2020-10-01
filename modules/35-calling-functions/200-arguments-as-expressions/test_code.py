import importlib
from hexlet.test import expect_output

def test(capsys):
    expected = '20'
    expect_output(capsys, expected)
