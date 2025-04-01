from hexlet.test import expect_output


def test(capsys):
    expected = "0.0858"
    expect_output(capsys, expected)
