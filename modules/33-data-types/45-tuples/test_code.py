from hexlet.test import expect_output


def test(capsys):
    expected = """From: Moscow
To: Saint Petersburg
Distance: 634 km"""

    expect_output(capsys, expected)
