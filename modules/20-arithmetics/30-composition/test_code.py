from hexlet.test import expect_output


def test(capsys):
    expected = "660"
    expect_output(capsys, expected)
