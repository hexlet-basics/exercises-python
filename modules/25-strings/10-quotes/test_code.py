from hexlet.test import expect_output


def test(capsys):
    expected = 'The file "user\'s_config.json" was not found.'
    expect_output(capsys, expected)
