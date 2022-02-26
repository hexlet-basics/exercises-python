import index


def test():
    assert index.get_random_number() >= 0
    assert index.get_random_number() <= 10
