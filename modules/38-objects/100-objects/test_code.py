from hexlet.test import expect_output


def test(capsys):
    expected = "the quick brown fox jumps over the lazy dog"
    expect_output(capsys, expected)
