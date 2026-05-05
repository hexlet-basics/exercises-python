from hexlet.test import expect_output


def test(capsys):
    expected = "0.30000000000000004"
    expect_output(capsys, expected)
