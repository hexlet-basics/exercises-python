import index


def test1():
    assert not index.is_pensioner(23)
    assert index.is_pensioner(70)
    assert index.is_pensioner(60)
    assert not index.is_pensioner(59)
