import index


def test():
    assert index.add_spaces("hex") == "h e x"
    assert index.add_spaces("Arya") == "A r y a"
    assert index.add_spaces("a") == "a"
