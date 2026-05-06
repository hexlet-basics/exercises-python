import index


def test1():
    assert index.sanitize_phone_number("+7 (999) 123-45-67") == "+79991234567"
    assert index.sanitize_phone_number("8 800 555 35 35") == "88005553535"
    assert index.sanitize_phone_number("(123) 456-7890") == "1234567890"
