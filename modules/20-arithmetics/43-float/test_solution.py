import importlib


def test(capsys):
    expected = "0.30000000000000004"
    expect_output(capsys, expected)


def expect_output(capsys, expected):
    importlib.import_module('solution')
    out, _err = capsys.readouterr()
    actual = out.strip('\n')

    with capsys.disabled():
        print('\n')
        print(out)

    assert actual == expected
