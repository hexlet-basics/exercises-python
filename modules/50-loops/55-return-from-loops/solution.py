def has_at_symbol(email: str) -> bool:
    index = 0
    while index < len(email):
        if email[index] == "@":
            return True
        index += 1
    return False
