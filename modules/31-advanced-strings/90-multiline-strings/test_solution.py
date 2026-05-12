import runpy


def test(capsys):
    expected = """Уважаемый пользователь!
Ваш заказ успешно оформлен.
Ожидаемая дата доставки: 3-5 рабочих дней.
Спасибо, что выбрали нас!"""
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
