from hexlet.test import expect_output


def test(capsys):
    expected = "4"
    expect_output(capsys, expected)
