def letter_multiply(text: str, letter: str, repetitions: int) -> str:
    result = []
    for char in text:
        char = letter * repetitions if char == letter else char
        result.append(char)
    return ''.join(result)
