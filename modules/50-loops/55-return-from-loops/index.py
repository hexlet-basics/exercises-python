def is_contains_char(string: str, char: str) -> bool:
    index = 0
    while index < len(string):
        if string[index] == char:
            return True
        index += 1
    return False
