from hexlet.test import TestEnv, assert_equal

with TestEnv() as env:
    is_falsy = env.expect_defined('is_falsy')
    assert_equal(is_falsy(''), True)
    assert_equal(is_falsy('a'), False)
    assert_equal(is_falsy(0), True)
    assert_equal(is_falsy(10), False)
