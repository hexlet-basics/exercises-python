import index


def test():
    assert index.truncate('hexlet', 2) == 'he...'
    assert index.truncate('it works!', 4) == 'it w...'
