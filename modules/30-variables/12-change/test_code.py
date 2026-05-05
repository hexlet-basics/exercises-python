from hexlet.test import expect_output


def test(capsys):
    expected = "доставлен"
    expect_output(capsys, expected)
