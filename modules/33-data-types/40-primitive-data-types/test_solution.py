import importlib


def test(capsys):
    expected = """Name: Anna
Birth year: 1994
Age: 32
Rating: 4.7"""
    expect_output(capsys, expected)


def expect_output(capsys, expected):
    importlib.import_module('solution')
    out, _err = capsys.readouterr()
    actual = out.strip('\n')

    with capsys.disabled():
        print('\n')
        print(out)

    assert actual == expected
