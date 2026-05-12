import runpy


def test(capsys):
    expected = """From: Moscow
To: Saint Petersburg
Distance: 634 km"""

    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
