def is_palindrome(word):
    lowerWord = word.lower()
    return lowerWord == lowerWord[::-1]


def is_not_palindrome(word):
    return not is_palindrome(word)
