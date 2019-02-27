def is_lannister_soldier(color, shield):
    return (color == 'red' and shield is None) or shield == 'lion'
