from hexlet.test import expect_output


def test(capsys):
    expected = """Name: Anna
Birth year: 1994
Age: 32
Rating: 4.7"""
    expect_output(capsys, expected)
