import importlib
from hexlet.test import expect_output


def test(capsys):
    expected = "- Did Joffrey agree?\n- He did. He also said \"I love using \\n\"."
    expect_output(capsys, expected)
