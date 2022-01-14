def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index].upper() == char.upper():
            count = count + 1
        index = index + 1
    return count
