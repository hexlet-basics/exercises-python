'''
Functions those an engine uses during testing
'''
__all__ = (
    'parent_for'
)


PARENTS  = {
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
