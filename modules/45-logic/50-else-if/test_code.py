from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    who_is_this_house_to_starks = env.expect_defined(
        'who_is_this_house_to_starks')
    assert_equal(who_is_this_house_to_starks('Tully'), 'friend')
    assert_equal(who_is_this_house_to_starks('Karstark'), 'friend')
    assert_equal(who_is_this_house_to_starks('Lannister'), 'enemy')
    assert_equal(who_is_this_house_to_starks('Martell'), 'neutral')
    assert_equal(who_is_this_house_to_starks('undefined'), 'neutral')
