from hexlet.code_basics import to_upper_case


# BEGIN
def filter_string(text, char):
    result = ''
    for current_char in text:
        if to_upper_case(current_char) != to_upper_case(char):
            result += current_char
    return result
# END
