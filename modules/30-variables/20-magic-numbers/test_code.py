from hexlet.test import expect_output


def test(capsys):
    expected = "Ящиков на складе:\n102"
    expect_output(capsys, expected)
