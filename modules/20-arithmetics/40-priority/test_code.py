from hexlet.test import expect_output


def test(capsys):
    expected = '49.0'
    expect_output(capsys, expected)
