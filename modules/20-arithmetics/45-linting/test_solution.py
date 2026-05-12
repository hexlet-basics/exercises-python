import runpy


def test(capsys):
    expected = "4"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
