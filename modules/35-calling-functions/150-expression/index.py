from hexlet.code_basics import calculate_distance

# BEGIN
winterfell_to_twins = calculate_distance('Winterfell', 'The Twins')
twins_to_eyrie = calculate_distance('The Twins', 'The Eyrie')
distance = winterfell_to_twins + twins_to_eyrie

print(distance)
# END
