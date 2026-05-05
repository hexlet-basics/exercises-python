from hexlet.test import expect_output


def test(capsys):
    expected = "https://hexlet.io\nhttps://hexlet.io"
    expect_output(capsys, expected)
