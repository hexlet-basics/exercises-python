from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    fun = env.expect_defined('custom_parent_for')
    assert_equal(fun('Cersei Lannister'), 'Tywin Lannister')
