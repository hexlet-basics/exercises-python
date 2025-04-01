from hexlet.test import expect_output


def test(capsys):
    expected = "10.12"
    expect_output(capsys, expected)
