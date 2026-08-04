
1. Implement a function called `is_palindrome()` that determines whether a word is a palindrome or not. A palindrome is a word that reads the same way in both directions. Words may be passed to the function in any case, so you must first convert the word to lowercase: `word.lower()`.

    ```python
    is_palindrome('level') # true
    is_palindrome('hexlet') # false
    is_palindrome('Racecar') # true
    is_palindrome('Function') # false
    ```

2. Implement a function called `is_not_palindrome()` which checks if a word is NOT a palindrome:

    ```python
    is_not_palindrome('radar') # false
    is_not_palindrome('level') # false
    is_not_palindrome('hexlet') # true
    ```

    To do this, call `is_palindrome()` inside `is_not_palindrome()` and apply negation.
