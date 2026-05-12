import runpy


def test(capsys):
    expected = "Здравствуйте, Анна! Ваш заказ #1337 принят."
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
