En un juego de palabras los participantes comprueban si una palabra es un palíndromo. Implementa dos funciones, `is_palindrome()` e `is_not_palindrome()`, que reciben una cadena de entrada

1. Implementa la función `is_palindrome()`, que determina si una palabra es un palíndromo o no. Un palíndromo es una palabra que se lee igual en los dos sentidos. A la función se le pueden pasar palabras en cualquier caso, por eso primero hay que convertir la palabra a minúsculas: `word.lower()`.

    ```python
    is_palindrome("ala")  # true
    is_palindrome("hexlet")  # false
    is_palindrome("Radar")  # true
    is_palindrome("función")  # false
    ```

2. Implementa la función `is_not_palindrome()`, que comprueba que una palabra NO es un palíndromo:

    ```python
    is_not_palindrome("ala")  # false
    is_not_palindrome("Radar")  # false
    is_not_palindrome("hexlet")  # true
    ```

    Para eso, llama a la función `is_palindrome()` dentro de `is_not_palindrome()` y aplica la negación.
