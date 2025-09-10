import index

def test1():
    assert not index.is_long_word("apple")  # 5 символов → False
    assert index.is_long_word("banana")  # 6 символов → True
    assert index.is_long_word("pineapple")  # 9 символов → True
