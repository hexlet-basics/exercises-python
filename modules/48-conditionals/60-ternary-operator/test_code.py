import index


def test1():
    assert index.flip_flop("flip") == "flop"
    assert index.flip_flop("flop") == "flip"
