from hexlet.test import expect_output


def test(capsys):
    expected = 'Coding has over 700 languages.'
    expect_output(capsys, expected)
