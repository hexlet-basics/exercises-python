from calendar import c


def test():
    with open('index.py') as file:
        comment = file.read() 
        assert comment == '# You know nothing, Jon Snow!\n'
        print(comment)
