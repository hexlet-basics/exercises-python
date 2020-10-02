from hexlet.test import expect_output


def test(capsys):
    expected = 'What Is Dead May Never Die'
    expect_output(capsys, expected)
