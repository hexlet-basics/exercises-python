from hexlet.test import expect_output


def test(capsys):
    expected = '87'
    expect_output(capsys, expected)
