import importlib


def check(output):
    value = int(output)

    assert value >= 0
    assert value <= 10


def test(capsys):
    importlib.import_module('solution')
    out, _ = capsys.readouterr()

    with capsys.disabled():
        print('\n')
        print(out)

    check(out.strip('\n'))
