from hexlet.test import expect_output


def test(capsys):
    expected = '80'
    expect_output(capsys, expected)
