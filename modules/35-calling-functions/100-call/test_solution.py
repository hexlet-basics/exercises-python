import runpy


def test(capsys):
    expected = "12"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
