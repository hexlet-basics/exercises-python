from hexlet.test import expect_output


def test(capsys):
    expected = 'Index Of N: 0\nIndex Of ,: 25'
    expect_output(capsys, expected)
