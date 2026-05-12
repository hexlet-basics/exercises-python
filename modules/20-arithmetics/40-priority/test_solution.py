import runpy


def test(capsys):
    expected = "160.0"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
