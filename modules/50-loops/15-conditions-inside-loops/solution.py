def count_hashtags(text: str) -> int:
    index = 0
    count = 0
    while index < len(text):
        if text[index] == "#":
            count = count + 1
        index = index + 1
    return count
