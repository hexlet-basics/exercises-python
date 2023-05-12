from hexlet.test import expect_output


def test(capsys):
    expected = '125.0\n863.75'
    expect_output(capsys, expected)
