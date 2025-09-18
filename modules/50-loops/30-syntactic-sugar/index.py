def filter_string(text: str, char: str) -> str:
    index = 0
    result = ""
    while index < len(text):
        current_char = text[index]
        if current_char != char:
            result = f"{result}{current_char}"
        index += 1
    return result
