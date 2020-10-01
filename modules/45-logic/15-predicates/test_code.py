from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    is_mister = env.expect_defined('is_mister')
    assert_equal(is_mister('8234782'), False)
    assert_equal(is_mister('Joker'), False)
    assert_equal(is_mister('Mister'), True)
