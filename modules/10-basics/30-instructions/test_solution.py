import runpy


def test(capsys):
    expected = "Заказ №1337\nСтатус: доставляется\nПримерный срок: 2 дня"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
