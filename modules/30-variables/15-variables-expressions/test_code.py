from hexlet.test import expect_output


def test(capsys):
    expected = '125.0\n7500.0'
    expect_output(capsys, expected)
