from hexlet.test import expect_output


def test(capsys):
    expected = "https://github.com/hexlet/exercises-python"
    expect_output(capsys, expected)
