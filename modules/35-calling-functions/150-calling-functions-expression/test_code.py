from hexlet.test import expect_output


def test(capsys):
    expected = "First: H\nLast: !"
    expect_output(capsys, expected)
