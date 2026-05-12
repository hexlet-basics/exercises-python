import solution


def test(capsys):
    solution.say_hello()
    expected = "Hello, World!"
    out, _ = capsys.readouterr()
    assert out.strip() == expected
