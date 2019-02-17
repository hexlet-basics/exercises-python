from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    fun = env.expect_defined('get_none')
    assert_equal(fun(), None)
