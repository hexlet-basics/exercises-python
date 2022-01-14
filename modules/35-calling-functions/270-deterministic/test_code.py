import importlib


def expect_output(capsys, expected):
    importlib.import_module('index')
    out, _err = capsys.readouterr()
    actual = out.strip()

    assert actual in expected

    print("\n")
    print(out)


def test(capsys):
    i = 0
    expected = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
    while i < 10:
        expect_output(capsys, expected)
        i += 1
