import runpy


def test(capsys):
    expected = "256\n3.0"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
