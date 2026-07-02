import importlib


def test(capsys):
    expected = 'Для разделения строк используйте "\\n"\nПример: print("строка1\\nстрока2")'
    expect_output(capsys, expected)


def expect_output(capsys, expected):
    importlib.import_module('solution')
    out, _err = capsys.readouterr()
    actual = out.strip('\n')

    with capsys.disabled():
        print('\n')
        print(out)

    assert actual == expected
