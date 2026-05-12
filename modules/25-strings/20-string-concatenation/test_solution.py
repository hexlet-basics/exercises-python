import runpy


def test(capsys):
    expected = "https://github.com/hexlet/exercises-python"
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
