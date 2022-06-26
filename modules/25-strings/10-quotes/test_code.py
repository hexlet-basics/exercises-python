from hexlet.test import expect_output


def test(capsys):
    expected = '"Khal Drogo\'s favorite word is "athjahakar""'
    expect_output(capsys, expected)
