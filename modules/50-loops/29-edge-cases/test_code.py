import index


def test1():
    string = 'Sansa Stark'
    end = len(string) - 1
    assert not index.is_arguments_for_substr_correct(string, -1, 0)
    assert not index.is_arguments_for_substr_correct(string, 0, -1)
    assert not index.is_arguments_for_substr_correct(string, end + 1, 0)
    assert not index.is_arguments_for_substr_correct(string, end, 5)
    assert index.is_arguments_for_substr_correct(string, end, 1)
    assert index.is_arguments_for_substr_correct(string, 3, 3)
    assert index.is_arguments_for_substr_correct(string, 0, 3)
    assert index.is_arguments_for_substr_correct(string, 0, 1)
    assert index.is_arguments_for_substr_correct(string, 0, 0)
