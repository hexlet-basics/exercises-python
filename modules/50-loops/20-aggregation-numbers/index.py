def multiply_numbers_from_range(start: int, finish: int) -> int:
    i = start
    result = 1
    while i <= finish:
        result = result * i
        i = i + 1
    return result
