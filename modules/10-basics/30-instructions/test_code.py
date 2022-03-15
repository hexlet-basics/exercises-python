from hexlet.test import expect_output


def test(capsys):
    expected = 'Roman\nMichael\nStephen'
    expect_output(capsys, expected)
