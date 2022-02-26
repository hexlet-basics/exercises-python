import index


def test():
    assert index.truncate('текст', 3) == 'тек...'
    assert index.truncate('и пошла вода', 5) == 'и пош...'
