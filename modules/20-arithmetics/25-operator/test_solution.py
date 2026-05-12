import runpy


def test(capsys):
    expected = "87\n29.0"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
