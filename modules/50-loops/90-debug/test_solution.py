from solution import compress


def test():
    assert compress("aaabcccc") == "a3bc4"
    assert compress("abcd") == "abcd"
    assert compress("aabbaa") == "a2b2a2"
    assert compress("a") == "a"
    assert compress("") == ""
    assert compress("zzz") == "z3"
