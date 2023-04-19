import index


def test():
    expected = [str, str, int, str]
    annotations = index.letter_multiply.__annotations__
    print(annotations)
    assert list(annotations.values()) == expected, 'You should use type annotations!'  # noqa: E501

    assert index.letter_multiply('python', 'p', 3) == 'pppython'
    assert index.letter_multiply('python', 'o', 4) == 'pythoooon'
    assert index.letter_multiply('java', 'a', 2) == 'jaavaa'
    assert index.letter_multiply('java', 'a', 0) == 'jv'
