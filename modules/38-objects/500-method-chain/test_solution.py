import runpy


def test(capsys):
    expected = "7"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
