import index


def test():
    expected = "hurray! hurray! hurray!"
    assert index.say_hurray_three_times() == expected
