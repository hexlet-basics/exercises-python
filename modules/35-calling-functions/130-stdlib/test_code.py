from hexlet.test import expect_output


def test(capsys):
    expected = "<class 'str'>"
    expect_output(capsys, expected)
