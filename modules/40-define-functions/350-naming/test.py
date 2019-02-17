from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    fun = env.expect_defined('get_formatted_birthday')
    assert_equal(fun(1, 1, 2001), '01-01-2001')
