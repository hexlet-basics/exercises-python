from hexlet.test import expect_output


def test(capsys):
    expected = "Заказ №1337\nСтатус: доставляется\nПримерный срок: 2 дня"
    expect_output(capsys, expected)
