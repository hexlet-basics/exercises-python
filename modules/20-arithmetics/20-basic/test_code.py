from hexlet.test import expect_output


def test(capsys):
    expected = '9.0'
    expect_output(capsys, expected)
