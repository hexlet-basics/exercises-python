import runpy


def test(capsys):
    expected = "125.0\n863.75"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
