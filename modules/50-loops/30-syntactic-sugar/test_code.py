import index


def test1():
    text = "one two three four five"
    assert index.filter_string(text, "x") == "one two three four five"
    assert index.filter_string(text, "e") == "on two thr four fiv"
    assert index.filter_string("zz zorro", "z") == " orro"
