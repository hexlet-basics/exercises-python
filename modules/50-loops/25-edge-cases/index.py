def is_arguments_for_substr_correct(string, index, length):
    return False if index < 0 or index + length > len(string) else True
