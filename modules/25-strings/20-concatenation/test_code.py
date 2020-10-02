from hexlet.test import expect_output


def test(capsys):
    expected = 'Winter came for the House of Frey.'
    expect_output(capsys, expected)
