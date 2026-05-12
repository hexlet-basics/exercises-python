import runpy


def test(capsys):
    expected = "36 °C"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
