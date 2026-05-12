import runpy


def test(capsys):
    expected = "10"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
