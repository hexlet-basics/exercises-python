import runpy


def test(capsys):
    expected = "0.30000000000000004"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
