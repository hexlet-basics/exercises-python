from hexlet.test import expect_output


def test(capsys):
    expected = '-0.304'
    expect_output(capsys, expected)
