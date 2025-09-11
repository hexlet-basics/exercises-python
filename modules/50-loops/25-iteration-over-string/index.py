def add_spaces(text):
    result = ""
    i = 0
    while i < len(text):
        if i > 0:
            result = result + " "
        result = result + text[i]
        i = i + 1
    return result
