import solution


def test1():
    assert solution.count_hashtags("New post #python #code") == 2
    assert solution.count_hashtags("No tags here") == 0
    assert solution.count_hashtags("#start and #finish") == 2
    assert solution.count_hashtags("###") == 3
