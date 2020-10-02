from hexlet.test import expect_output


def test(capsys):
    expected = 'King Balon the 6th has 102 rooms.'
    expect_output(capsys, expected)
