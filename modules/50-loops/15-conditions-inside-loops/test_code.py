import index


def test1():
    assert index.count_hashtags("New post #python #code") == 2
    assert index.count_hashtags("No tags here") == 0
    assert index.count_hashtags("#start and #finish") == 2
    assert index.count_hashtags("###") == 3
