def get_even_numbers_up_to(number):
    counter = 1
    result = ''
    while counter <= number:
        if counter % 2 == 0:
            result = result + str(counter) + ','
        counter += 1
    return result
