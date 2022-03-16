from hexlet.test import expect_output


def test(capsys):
    expected = 'Everything is interesting if you go into it deeply enough'
    expect_output(capsys, expected)
