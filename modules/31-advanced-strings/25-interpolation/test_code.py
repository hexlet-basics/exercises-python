from hexlet.test import expect_output


def test(capsys):
    expected = "Здравствуйте, Анна! Ваш заказ #1337 принят."
    expect_output(capsys, expected)
