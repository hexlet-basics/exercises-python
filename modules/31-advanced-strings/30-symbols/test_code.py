from hexlet.test import expect_output


def test(capsys):
    expected = "s"
    expect_output(capsys, expected)
