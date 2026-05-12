import solution


def test1():
    assert not solution.is_long_word("apple")  # 5 символов → False
    assert solution.is_long_word("banana")  # 6 символов → True
    assert solution.is_long_word("pineapple")  # 9 символов → True
