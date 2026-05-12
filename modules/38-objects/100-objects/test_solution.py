import runpy


def test(capsys):
    expected = "the quick brown fox jumps over the lazy dog"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
