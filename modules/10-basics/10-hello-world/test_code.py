from hexlet.test import expect_output


def test(capsys):
    expected = 'Hello, World!'
    expect_output(capsys, expected)
