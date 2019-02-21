# BEGIN
def count_chars(string, char):
    index = len(string) - 1
    result = 0
    while index >= 0:
        if string[index] == char:
            result += 1
        index -= 1
    return result
# END
