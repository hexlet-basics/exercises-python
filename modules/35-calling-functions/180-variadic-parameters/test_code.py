from hexlet.test import expect_output


def test(capsys):
    expected = "-3"
    expect_output(capsys, expected)
