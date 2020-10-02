from hexlet.test import expect_output


def test(capsys):
    expected = 'Targaryen\n and \nDragon'
    expect_output(capsys, expected)
