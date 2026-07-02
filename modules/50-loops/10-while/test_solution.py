import solution


def test1(capsys):
    solution.print_countdown(2)
    out, _ = capsys.readouterr()

    with capsys.disabled():
        print('\n')
        print(out)

    assert out.strip('\n') == "2\n1\nGo!"


def test2(capsys):
    solution.print_countdown(4)
    out, _ = capsys.readouterr()

    with capsys.disabled():
        print('\n')
        print(out)

    assert out.strip('\n') == "4\n3\n2\n1\nGo!"
