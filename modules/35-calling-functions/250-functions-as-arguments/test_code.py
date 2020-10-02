from hexlet.test import expect_output


def test(capsys):
    expected = 'Tywin Lannister'
    expect_output(capsys, expected)
