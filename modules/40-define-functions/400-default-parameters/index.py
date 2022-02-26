def get_hidden_card(cardNumber, starsCount=4):
    visibleDigitsLine = cardNumber[-4:]
    return f"{'*' * starsCount}{visibleDigitsLine}"
