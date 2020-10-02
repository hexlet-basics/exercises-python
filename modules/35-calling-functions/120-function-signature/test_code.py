from hexlet.test import expect_output


def test(capsys):
    expected = '0xff'
    expect_output(capsys, expected)
