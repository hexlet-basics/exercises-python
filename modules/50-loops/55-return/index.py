# BEGIN
def does_contain(string, char):
    index = 0
    while index < len(string):
        if string[index] == char:
            return True
        index += 1
    return False
# END
