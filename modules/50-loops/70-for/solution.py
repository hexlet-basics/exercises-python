def normalize_filename(filename: str) -> str:
    result = ""
    for current_char in filename:
        if current_char == " ":
            result += "_"
        else:
            result += current_char
    return result
