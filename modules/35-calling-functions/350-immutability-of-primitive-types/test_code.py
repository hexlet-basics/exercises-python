import importlib
from hexlet.test import expect_output

def test(capsys):
    expected = '0x2a'
    expect_output(capsys, expected)
