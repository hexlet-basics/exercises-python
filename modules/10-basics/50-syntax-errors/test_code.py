from hexlet.test import expect_output


def test(capsys):
    expected = 'The best error message is the one that never shows up.'
    expect_output(capsys, expected)
