def get_number_explanation(number):
    match number:
        case 666:
            return "devil number"
        case 7:
            return "prime number"
        case 42:
            return "answer for everything"
        case _:
            return "just a number"
