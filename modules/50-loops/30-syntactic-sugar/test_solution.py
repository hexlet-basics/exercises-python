import solution


def test1():
    assert solution.build_progress_bar(0, 5) == "-----"
    assert solution.build_progress_bar(3, 5) == "###--"
    assert solution.build_progress_bar(5, 5) == "#####"
