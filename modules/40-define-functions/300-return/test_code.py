import index


def test1():
    actual = index.get_parent_names_total_length('Daenerys Targaryen')
    expected = 35
    assert actual == expected
