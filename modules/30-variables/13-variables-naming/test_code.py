from hexlet.test import expect_output


def test(capsys):
    expected = "2"
    expect_output(capsys, expected)
