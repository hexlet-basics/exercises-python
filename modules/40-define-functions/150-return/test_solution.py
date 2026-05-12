import solution

def test():
    assert solution.truncate("hexlet", 2) == "he..."
    assert solution.truncate("it works!", 4) == "it w..."
