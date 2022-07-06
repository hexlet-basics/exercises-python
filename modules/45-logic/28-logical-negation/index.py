def is_palindrome(word):
    lower_word = word.lower()
    return lower_word == lower_word[::-1]


def is_not_palindrome(word):
    return not is_palindrome(word)
