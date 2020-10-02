from hexlet.test import expect_output


def test(capsys):
    expected = '9780262531962'
    expect_output(capsys, expected)
