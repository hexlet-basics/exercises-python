def test():
    with open("solution.py") as file:
        comment = file.read().rstrip()
        assert comment == "# TODO: добавить функцию приветствия"
        print(comment)
