import solution


def test():
    assert solution.trim_and_repeat("python") == "python"
    assert solution.trim_and_repeat("python", offset=4) == "on"
    assert solution.trim_and_repeat("python", repetitions=2) == "pythonpython"
    assert (
        solution.trim_and_repeat("python", offset=4, repetitions=2) == "onon"
    )
