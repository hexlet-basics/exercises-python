import runpy


def test(capsys):
    expected = 'The file "user\'s_config.json" was not found.'
    runpy.run_module('solution')
    out, _ = capsys.readouterr()
    assert out.strip() == expected
