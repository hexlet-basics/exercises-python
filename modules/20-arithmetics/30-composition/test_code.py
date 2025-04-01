from hexlet.test import expect_output


def test(capsys):
    expected = "10.5"
    expect_output(capsys, expected)
