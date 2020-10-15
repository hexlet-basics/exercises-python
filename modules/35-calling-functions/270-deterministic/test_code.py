from hexlet.test import expect_output


def test(capsys):
    expected = 'KNOCK!'
    expect_output(capsys, expected)
