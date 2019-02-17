from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    fun = env.expect_defined('get_age_difference')
    assert_equal(fun(2001, 2018), 'The age difference is 17')
