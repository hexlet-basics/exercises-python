import index


def test1():
    assert index.build_progress_bar(0, 5) == "-----"
    assert index.build_progress_bar(3, 5) == "###--"
    assert index.build_progress_bar(5, 5) == "#####"
