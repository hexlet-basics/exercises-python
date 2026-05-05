def test():
    with open("index.py") as file:
        comment = file.read().rstrip()
        assert comment == "# TODO: добавить функцию приветствия"
        print(comment)
