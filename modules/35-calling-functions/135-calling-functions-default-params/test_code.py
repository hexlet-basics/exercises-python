from hexlet.test import expect_output


def test(capsys):
    expected = "37.8\n2426.76\n607"
    expect_output(capsys, expected)
