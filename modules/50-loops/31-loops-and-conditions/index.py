# BEGIN
def shouter(string):
    length = len(string)
    result = ''
    if 0 < length < 5:
        result = string
    elif length == 5:
        counter = 0
        counter_limit = 10
        while counter != counter_limit:
            result += string
            counter += 1
    elif length > 5:
        counter = 0
        counter_limit = 100
        while counter != counter_limit:
            result += string
            counter += 1
    return result
# END
