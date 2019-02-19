from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    in_neutral_soldier = env.expect_defined('in_neutral_soldier')
    assert_equal(in_neutral_soldier('Tully'), 'friend')
    assert_equal(in_neutral_soldier('Karstark'), 'friend')
    assert_equal(in_neutral_soldier('Lannister'), 'enemy')
    assert_equal(in_neutral_soldier('Martell'), 'neutral')
    assert_equal(in_neutral_soldier('undefined'), 'neutral')
