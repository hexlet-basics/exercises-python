from hexlet.test import expect_output


def test(capsys):
    expected = "Программа успешно запущена"
    expect_output(capsys, expected)
