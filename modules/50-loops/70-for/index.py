def filter_string(text: str, char: str) -> str:
    result = ""
    for current_char in text:
        if current_char.upper() != char.upper():
            result += current_char
    return result
