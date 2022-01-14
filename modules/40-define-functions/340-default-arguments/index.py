# BEGIN
def get_hidden_card(card_number, stars_count=4):
    visible_digits = card_number[-4:]
    return visible_digits.rjust(stars_count + 4, '*')
# END
