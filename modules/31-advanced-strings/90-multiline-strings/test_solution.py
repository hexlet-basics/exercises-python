import importlib


def test(capsys):
    expected = """Уважаемый пользователь!
Ваш заказ успешно оформлен.
Ожидаемая дата доставки: 3-5 рабочих дней.
Спасибо, что выбрали нас!"""
    expect_output(capsys, expected)


def expect_output(capsys, expected):
    importlib.import_module('solution')
    out, _err = capsys.readouterr()
    actual = out.strip('\n')

    with capsys.disabled():
        print('\n')
        print(out)

    assert actual == expected
