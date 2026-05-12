import runpy


def test(capsys):
    expected = "Hello, World!"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
