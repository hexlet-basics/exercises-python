import runpy


def test(capsys):
    expected = "grip"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
