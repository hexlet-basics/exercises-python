def compress(string: str) -> str:
    if not string:
        return ""

    result = ""
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            result += string[i - 1]
            if count > 1:
                result += str(count)
            count = 1

    result += string[-1]
    if count > 1:
        result += str(count)

    return result
