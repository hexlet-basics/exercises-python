import solution


def test1():
    assert not solution.is_not_palindrome("wow")
    assert solution.is_not_palindrome("hexlet")
    assert not solution.is_not_palindrome("asdffdsa")
    assert not solution.is_not_palindrome("Wow")
    assert solution.is_not_palindrome("CodeBasics")
