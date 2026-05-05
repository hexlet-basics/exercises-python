from hexlet.test import expect_output


def test(capsys):
    expected = """Здравствуйте, Анна!
Спасибо за ваш заказ.
Ожидаемая дата доставки — 3 рабочих дня."""
    expect_output(capsys, expected)
