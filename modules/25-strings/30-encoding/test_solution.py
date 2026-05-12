import runpy


def test(capsys):
    expected = "~\n^\n%"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
