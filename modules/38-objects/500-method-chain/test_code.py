from hexlet.test import expect_output


def test(capsys):
    expected = '8'
    expect_output(capsys, expected)
