import importlib


def test(capsys):
    expected = """Hello, Anna!
Thank you for your order.
Estimated delivery date — 3 business days."""
    expect_output(capsys, expected)


def expect_output(capsys, expected):
    importlib.import_module('solution')
    out, _err = capsys.readouterr()
    actual = out.strip('\n')

    with capsys.disabled():
        print('\n')
        print(out)

    assert actual == expected
