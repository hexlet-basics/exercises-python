import index


def test():
    actual1 = index.get_hidden_card('1234123412341234')
    assert actual1 == '****1234'

    actual2 = index.get_hidden_card('1234123412344321', 6)
    assert actual2 == '******4321'
