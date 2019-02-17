from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    fun = env.expect_defined('get_parent_names_total_length')
    assert_equal(fun('Daenerys Targaryen'), 35)
