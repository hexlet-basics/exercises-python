from hexlet.test import expect_output


def test(capsys):
    expected = '243\n2.0'
    expect_output(capsys, expected)
