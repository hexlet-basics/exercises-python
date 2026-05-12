import solution


def test1():
    assert solution.guess_number(100500) == "Try again!"
    assert solution.guess_number(42) == "You win!"
