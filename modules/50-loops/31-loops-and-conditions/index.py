def shouter(string):
    length = len(string)

    if length == 0:
        counter = 0
    elif 0 < length < 5:
        counter = 1
    elif length == 5:
        counter = 10
    else:
        counter = 100

    result = ''
    while counter > 0:
        result += string
        counter -= 1

    return result
