from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    is_pensioner = env.expect_defined('is_pensioner')
    assert_equal(is_pensioner(23), False)
    assert_equal(is_pensioner(70), True)
    assert_equal(is_pensioner(60), True)
    assert_equal(is_pensioner(59), False)
