from hexlet.test import expect_output


def test(capsys):
    expected = "Rooms in King Balon's Castle:\n102"
    expect_output(capsys, expected)
