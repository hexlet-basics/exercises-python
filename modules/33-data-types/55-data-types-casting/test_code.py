from hexlet.test import expect_output


def test(capsys):
    expected = "2 times"
    expect_output(capsys, expected)
