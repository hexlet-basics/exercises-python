import importlib
from hexlet.test import expect_output

def test(capsys):
    expected = 'Rhaella Targaryen'
    expect_output(capsys, expected)
