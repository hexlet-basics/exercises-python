
En esta lección, deberás implementar dos funciones: is_palindrome()` y `is_not_palindrome()`

1. Implementa la función `is_palindrome()`, que determina si una palabra es un palíndromo o no. Un palíndromo es una palabra que se lee igual en ambos sentidos. Las palabras pueden estar en cualquier caso, por lo que primero debes convertir la palabra a minúsculas: `word.lower()`.

    ```python
    is_palindrome('ala') # true
    is_palindrome('hexlet') # false
    is_palindrome('radar') # true
    is_palindrome('función') # false
    ```

2. Implementa la función `is_not_palindrome()`, que verifica que una palabra NO sea un palíndromo:

    ```python
    is_not_palindrome('radar') # false
    is_not_palindrome('ala') # false
    is_not_palindrome('hexlet') # true
    ```

    Para hacer esto, llama a la función `is_palindrome()` dentro de `is_not_palindrome()` y aplica la negación.
