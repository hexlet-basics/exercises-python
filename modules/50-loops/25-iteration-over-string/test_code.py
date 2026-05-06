import index


def test():
    assert index.mask_card_number("1234567812345678") == "************5678"
    assert index.mask_card_number("12345678") == "****5678"
    assert index.mask_card_number("0000111122223333") == "************3333"
