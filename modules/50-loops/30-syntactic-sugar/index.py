def filter_string(string, char):
    index = 0
    result = ''
    while index < len(string):
        current_char = string[index]
        if current_char != char:
            result += current_char
        index += 1
    return result
