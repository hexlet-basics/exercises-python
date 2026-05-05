from hexlet.test import expect_output


def test(capsys):
    expected = "print"
    expect_output(capsys, expected)
