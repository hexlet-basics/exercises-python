import runpy


def test(capsys):
    expected = "37.8\n2426.76\n607"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
