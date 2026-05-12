import runpy


def test(capsys):
    expected = "First: H\nLast: !"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
