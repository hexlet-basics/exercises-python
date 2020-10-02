import index


def test1():
    assert not index.has_targaryen_reference('')
    assert not index.has_targaryen_reference('Targari')
    assert not index.has_targaryen_reference('targaryen')
    assert index.has_targaryen_reference('Targaryens')
    assert index.has_targaryen_reference('Targaryen')
