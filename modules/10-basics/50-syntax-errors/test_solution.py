import runpy


def test(capsys):
    expected = "Программа успешно запущена"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
