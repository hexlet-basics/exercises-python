from hexlet.test import expect_output


def test(capsys):
    expected = '~\n^\n%'
    expect_output(capsys, expected)
