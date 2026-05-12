import runpy


def test(capsys):
    expected = """Name: Anna
Birth year: 1994
Age: 32
Rating: 4.7"""
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
