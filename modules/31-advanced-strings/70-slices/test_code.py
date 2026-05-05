from hexlet.test import expect_output


def test(capsys):
    expected = "hexlet.io"
    expect_output(capsys, expected)
