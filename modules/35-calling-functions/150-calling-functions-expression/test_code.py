from hexlet.test import expect_output


def test(capsys):
    expected = "First: N\nLast: t"
    expect_output(capsys, expected)
