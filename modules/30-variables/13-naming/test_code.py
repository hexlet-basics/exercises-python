from hexlet.test import expect_output


def test(capsys):
    expected = '-2000'
    expect_output(capsys, expected)
