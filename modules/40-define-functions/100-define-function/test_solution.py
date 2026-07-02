import solution


def test(capsys):
    expected = "Hello, World!"
    solution.say_hello()
    out, _ = capsys.readouterr()

    with capsys.disabled():
        print('\n')
        print(out)

    assert out.strip('\n') == expected
