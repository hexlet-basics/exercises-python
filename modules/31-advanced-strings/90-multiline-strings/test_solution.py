import importlib


def test(capsys):
    expected = """Dear customer!
Your order has been placed successfully.
Estimated delivery date: 3-5 business days.
Thank you for choosing us!"""
    expect_output(capsys, expected)


def expect_output(capsys, expected):
    importlib.import_module('solution')
    out, _err = capsys.readouterr()
    actual = out.strip('\n')

    with capsys.disabled():
        print('\n')
        print(out)

    assert actual == expected
