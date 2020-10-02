from hexlet.test import expect_output


def test(capsys):
    expected = 'Robert\nStannis\nRenly'
    expect_output(capsys, expected)
