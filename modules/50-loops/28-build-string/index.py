def my_substr(string, length):
    result_string = ""
    index = 0
    while index < length:
        result_string = result_string + string[index]
        index = index + 1

    return result_string
