import index


def test1():
    assert index.who_is_this_house_to_starks('Tully') == 'friend'
    assert index.who_is_this_house_to_starks('Karstark') == 'friend'
    assert index.who_is_this_house_to_starks('Lannister') == 'enemy'
    assert index.who_is_this_house_to_starks('Martell') == 'neutral'
    assert index.who_is_this_house_to_starks('undefined') == 'neutral'
