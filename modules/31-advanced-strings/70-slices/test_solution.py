import runpy


def test(capsys):
    expected = "hexlet.io"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
