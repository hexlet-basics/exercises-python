from hexlet.test import expect_output


def test(capsys):
    expected = 'xle'
    expect_output(capsys, expected)
