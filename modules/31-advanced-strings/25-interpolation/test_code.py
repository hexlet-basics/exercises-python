from hexlet.test import expect_output


def test(capsys):
    expected = "Do you want to eat, Arya?"
    expect_output(capsys, expected)
