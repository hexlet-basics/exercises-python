from hexlet.test import expect_output


def test(capsys):
    expected = """Уважаемый пользователь!
Ваш заказ успешно оформлен.
Ожидаемая дата доставки: 3-5 рабочих дней.
Спасибо, что выбрали нас!"""
    expect_output(capsys, expected)
