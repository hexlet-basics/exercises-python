import index


def test1():
    assert index.get_number_explanation(0) == 'just a number'
    assert index.get_number_explanation(666) == 'devil number'
    assert index.get_number_explanation(42) == 'answer for everything'
    assert index.get_number_explanation(7) == 'prime number'
