from hexlet.test import expect_output


def test(capsys):
    expected = 'hodor'
    expect_output(capsys, expected)
