'''
Functions those an engine uses during testing
'''
__all__ = (
    'calculate_distance',
    'calculate_distance_between_towns',
    'is_lannister_soldier',
    'parent_for',
    'to_upper_case',
    'get_current_date',
)


PARENTS = {
    'Daenerys Targaryen': {
        'mother': 'Rhaella Targaryen',
        'father': 'Aerys II Targaryen',
    },
    'Cersei Lannister': {
        'father': 'Tywin Lannister'
    },
    'Joffrey Baratheon': {
        'mother': 'Cersei Lannister'
    }
}


def parent_for(child_name: str, parent_name: str = 'mother') -> str:
    '''
    Returns a parent (name) for the child.
    '''
    if parent_name not in ('mother', 'father'):
        raise ValueError('Wrong parent\'s name: ' + parent_name)
    try:
        return PARENTS[child_name][parent_name]
    except KeyError:
        raise ValueError('Wrong child\'s name: ' + child_name)


def calculate_distance(source: str, dest: str) -> int:
    '''
    Returns a distance between two towns.
    '''
    cities = winterfell, twins, eyrie, qarth, dothrak = [
        'Winterfell', 'The Twins', 'The Eyrie', 'Qarth', 'Vaes Dothrak']

    unknown_city = 'Unknown city: {} Please check city name.'

    if source not in cities:
        raise ValueError(unknown_city.format(source))
    if dest not in cities:
        raise ValueError(unknown_city.format(dest))

    def from_to(town1, town2):
        return (source, dest) in ((town1, town2), (town2, town1))

    distance = (
        (from_to(winterfell, twins) and 60) or
        (from_to(twins, eyrie) and 20) or
        (from_to(qarth, dothrak) and 125)
    )
    if not distance:
        unknown_distance = '''Unknown distance between cities {} and {}.
Please ask for a distance between some other pair of cities.'''
        raise ValueError(unknown_distance.format(source, dest))
    return distance


def calculate_distance_between_towns(param: str) -> int:
    '''
    Returns a distance between two towns. Accepts a road name in format
    "A-B"
    '''
    source, dest = param.split('-', 1)
    return calculate_distance(source, dest)


def is_lannister_soldier(color: str, shield: str = None) -> bool:
    '''
    Checks that soldier is from Lannister's army
    '''
    return (color == 'red' and shield is None) or shield == 'lion'


def to_upper_case(text: str) -> str:
    '''
    Converts all lowercase characters in a string into uppercase
    '''
    return text.upper()
