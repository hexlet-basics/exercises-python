def fizzbuzz(n):
    result = ""
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            word = "FizzBuzz"
        elif i % 3 == 0:
            word = "Fizz"
        elif i % 5 == 0:
            word = "Buzz"
        else:
            word = str(i)

        if result == "":
            result = word
        else:
            result += " " + word
    return result
