import index

STRING1 = 'A'
STRING2 = 'HELLO'
STRING3 = 'HELLO!'

SHOUT_STRING1 = 'A'
SHOUT_STRING2 = 'HELLO' * 10
SHOUT_STRING3 = 'HELLO!' * 100


def test1():
    assert index.shouter(STRING1) == SHOUT_STRING1
    assert index.shouter(STRING2) == SHOUT_STRING2
    assert index.shouter(STRING3) == SHOUT_STRING3
