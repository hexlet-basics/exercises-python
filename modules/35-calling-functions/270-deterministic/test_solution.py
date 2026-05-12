import runpy


def check(output):
    value = int(output)

    assert value >= 0
    assert value <= 10


def test(capsys):
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    check(out.strip())
