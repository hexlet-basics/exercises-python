import index

def test1():
    assert index.get_even_numbers_up_to(9) == '2,4,6,8,'
    assert index.get_even_numbers_up_to(15) == '2,4,6,8,10,12,14,'
    assert index.get_even_numbers_up_to(2) == '2,'
