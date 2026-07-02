import importlib


def test(capsys):
    expected = "Здравствуйте, Анна! Ваш заказ #1337 принят."
    expect_output(capsys, expected)


def expect_output(capsys, expected):
    importlib.import_module('solution')
    out, _err = capsys.readouterr()
    actual = out.strip('\n')

    with capsys.disabled():
        print('\n')
        print(out)

    assert actual == expected
