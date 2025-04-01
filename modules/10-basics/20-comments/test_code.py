def test():
    with open("index.py") as file:
        comment = file.read().rstrip()
        assert comment == "# You know nothing, Jon Snow!"
        print(comment)
