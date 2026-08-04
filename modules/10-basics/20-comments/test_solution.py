def test():
    with open("solution.py") as file:
        comment = file.read().rstrip()
        assert comment == "# TODO: add a greeting function"
        print(comment)
