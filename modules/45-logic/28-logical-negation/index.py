def is_palindrome(word: str) -> bool:
    lower_word = word.lower()
    return lower_word == lower_word[::-1]


def is_not_palindrome(word: str) -> bool:
    return not is_palindrome(word)
