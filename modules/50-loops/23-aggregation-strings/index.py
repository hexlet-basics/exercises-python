def join_numbers_from_range(start, end):
    i = start
    result = ""
    while i <= end:
        result = result + str(i)
        i = i + 1
    return result
