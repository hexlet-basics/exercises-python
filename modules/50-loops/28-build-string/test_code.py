import index


def test1():
    assert index.my_substr("got", 3) == "got"
    assert index.my_substr("got", 2) == "go"
    assert index.my_substr("got", 1) == "g"
