from hexlet.test import expect_output


def test(capsys):
    expected = "\"Toto's favorite word is \"Hexlet\"\""
    expect_output(capsys, expected)
