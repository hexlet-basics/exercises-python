from hexlet.test import expect_output


def test(capsys):
    expected = "a mind needs books as a sword needs a whetstone."
    expect_output(capsys, expected)
