def sanitize_phone_number(phone: str) -> str:
    i = 0
    result = ""
    while i < len(phone):
        char = phone[i]
        if char not in " ()-":
            result += char
        i += 1
    return result
