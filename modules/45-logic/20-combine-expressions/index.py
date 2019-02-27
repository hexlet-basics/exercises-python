def has_targaryen_reference(string):
    length = len('Targaryen')
    prefix = string[:length]
    return prefix == 'Targaryen'
