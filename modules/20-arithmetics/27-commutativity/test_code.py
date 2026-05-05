from hexlet.test import expect_output


def test(capsys):
    expected = "256\n3.0"
    expect_output(capsys, expected)
