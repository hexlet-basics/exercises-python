import runpy


def test(capsys):
    expected = """Здравствуйте, Анна!
Спасибо за ваш заказ.
Ожидаемая дата доставки — 3 рабочих дня."""
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
