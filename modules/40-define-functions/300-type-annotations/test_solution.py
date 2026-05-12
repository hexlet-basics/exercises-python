import solution


def test():
    expected = [str, int, str]
    annotations = solution.word_multiply.__annotations__
    print(annotations)
    assert list(annotations.values()) == expected, "You should use type annotations!"  # noqa: E501

    assert solution.word_multiply("python", 1) == "python"
    assert solution.word_multiply("python", 3) == "pythonpythonpython"
    assert solution.word_multiply("java", 0) == ""
