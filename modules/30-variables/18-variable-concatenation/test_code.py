from hexlet.test import expect_output


def test(capsys):
    expected = """Hello, Joffrey!
Here is important information about your account security.
We couldn't verify your mother's maiden name."""
    expect_output(capsys, expected)
