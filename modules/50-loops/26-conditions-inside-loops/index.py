from hexlet.code_basics import to_upper_case

# BEGIN
def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if to_upper_case(string[index]) == to_upper_case(char):
            count = count + 1
        index = index + 1
    return count
# END
