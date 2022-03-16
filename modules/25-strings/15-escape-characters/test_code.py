from hexlet.test import expect_output


def test(capsys):
    expected = "- Did Toto agree?\n" \
               "- He did. He also said \"I love using \\n\"."
    expect_output(capsys, expected)
