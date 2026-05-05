from hexlet.test import expect_output


def test(capsys):
    expected = "grip"
    expect_output(capsys, expected)
