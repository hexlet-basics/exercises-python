from hexlet.test import expect_output


def test(capsys):
    expected = "Grigor"
    expect_output(capsys, expected)
