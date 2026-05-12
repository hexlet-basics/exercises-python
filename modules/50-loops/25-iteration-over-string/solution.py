def mask_card_number(card_number: str) -> str:
    result = ""
    i = 0
    visible_part_start = len(card_number) - 4
    while i < len(card_number):
        if i < visible_part_start:
            result += "*"
        else:
            result += card_number[i]
        i = i + 1
    return result
