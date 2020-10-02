from hexlet.test import expect_output


def test(capsys):
    expected = 'anneirB'
    expect_output(capsys, expected)
