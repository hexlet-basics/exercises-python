import runpy


def test(capsys):
    expected = "Ящиков на складе:\n102"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
