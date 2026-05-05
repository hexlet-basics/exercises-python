from hexlet.test import expect_output


def test(capsys):
    expected = "87\n29.0"
    expect_output(capsys, expected)
