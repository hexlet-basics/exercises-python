from hexlet.test import expect_output


def test(capsys):
    expected = '13'
    expect_output(capsys, expected)
