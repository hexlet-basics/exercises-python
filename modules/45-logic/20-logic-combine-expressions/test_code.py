import index


def test1():
    assert not index.is_international_phone("89602223423")
    assert index.is_international_phone("+79602223423")
