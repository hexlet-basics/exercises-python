import index


def test1():
    assert not index.is_not_palindrome('wow')
    assert index.is_not_palindrome('hexlet')
    assert index.is_not_palindrome('asdffdsa')
    assert not index.is_not_palindrome('Wow')
