import runpy


def test(capsys):
    expected = "доставлен"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
