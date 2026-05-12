import runpy


def test(capsys):
    expected = 'Для разделения строк используйте "\\n"\nПример: print("строка1\\nстрока2")'
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
