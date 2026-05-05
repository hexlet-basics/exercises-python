from hexlet.test import expect_output


def test(capsys):
    expected = "160.0"
    expect_output(capsys, expected)
