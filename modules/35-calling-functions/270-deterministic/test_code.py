from hexlet.test import expect_output


def check(output):
    value = int(output)

    assert value >= 0
    assert value <= 10


def test(capsys):
    expect_output(capsys, check)
