from hexlet.test import expect_output


def test(capsys):
    expected = "7"
    expect_output(capsys, expected)
