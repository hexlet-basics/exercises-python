import index


def test_class():
    person = index.Person('John', 20)
    assert person.name == 'John'
    assert person.age == 20
