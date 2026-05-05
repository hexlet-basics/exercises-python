import index


def test():
    assert index.add_spaces("hex") == "h e x"
    assert index.add_spaces("Anna") == "A n n a"
    assert index.add_spaces("a") == "a"
