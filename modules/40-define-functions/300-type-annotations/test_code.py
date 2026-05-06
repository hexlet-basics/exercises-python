import index


def test():
    expected = [str, int, str]
    annotations = index.word_multiply.__annotations__
    print(annotations)
    assert list(annotations.values()) == expected, "You should use type annotations!"  # noqa: E501

    assert index.word_multiply("python", 1) == "python"
    assert index.word_multiply("python", 3) == "pythonpythonpython"
    assert index.word_multiply("java", 0) == ""
